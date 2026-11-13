"""Run evaluator B or C over a dataset (D0, D1 or D2).

Both evaluators get the same base model, parameters, reference pack and input format;
they differ only in evaluators/{B,C}/method.md. The model never sees which system produced an answer.

Usage:
  python src/evaluate.py --config config.yaml --evaluator B --dataset D0
  python src/evaluate.py --config config.yaml --evaluator C --dataset D1 [--ids D1-Q1-EN-gpt-r1,...] [--mock]
Outputs: data/eval/<dataset>_<evaluator>.jsonl (+ raw/), resumable.
"""
import argparse, datetime as dt, hashlib, json, os, pathlib, re, sys, time

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATASETS = {"D0": ROOT / "data/D0/d0_responses_raw.jsonl",
            "D1": ROOT / "data/D1/responses.jsonl",
            "D2": ROOT / "data/D2/objects.jsonl"}


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ----------------------------------------------------------------------------- reference pack
def reference_pack(question):
    """Profiles + authority map + the question's own section + sources registry.
    Excluded: section 3 (meta review notes) and Q1.5 (claims harvested from D0 answers)."""
    text = (ROOT / "reference/reference_key.md").read_text(encoding="utf-8")
    parts = re.split(r"(?m)^## ", text)
    keep = []
    for p in parts[1:]:
        head = p.split("\n", 1)[0]
        if head.startswith(("0.", "1.", "2.")) or head.startswith(question + "."):
            if head.startswith("Q1."):
                p = re.sub(r"(?ms)^### Q1\.5 .*?(?=^### |\Z)", "", p)
            keep.append("## " + p.rstrip())
    return "# REFERENCE PACK (frozen reference-v1.0)\n\n" + "\n\n".join(keep)


def system_blocks(evaluator, question):
    common = (ROOT / "evaluators/common.md").read_text(encoding="utf-8")
    method = (ROOT / f"evaluators/{evaluator}/method.md").read_text(encoding="utf-8")
    pack = reference_pack(question)
    # pack first so B and C share the cached prefix for a question
    return [{"type": "text", "text": pack, "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": common + "\n\n" + method, "cache_control": {"type": "ephemeral"}}]


# ----------------------------------------------------------------------------- items
def load_items(dataset, path):
    prompts = json.loads((ROOT / "prompts/prompts_D1.json").read_text(encoding="utf-8"))
    def prompt_for(q, lang):
        node = prompts.get(q) or prompts.get("questions", {}).get(q) or {}
        return node.get(lang) or node.get("prompt", {}).get(lang, "")
    items = []
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if dataset == "D0":
            if r.get("completeness") == "no":
                continue  # discarded capture (not in the canonical 18)
            q, lang = "Q1", r["language"]
            cites = r.get("citations")
            cit_text = (cites if isinstance(cites, str) else json.dumps(cites, ensure_ascii=False)) or "none"
            items.append({"id": r["id"], "question": q, "language": lang,
                          "prompt": prompt_for(q, lang), "answer": r["text_raw"],
                          "citations": "Citation chips visible in the chat interface (labels only, no quoted text): "
                                       + cit_text})
        else:
            text = r["response_text"]
            lines = []
            for k, c in enumerate(r.get("citations") or [], 1):
                frag = text[c["start"]:c["end"]] if c.get("start") is not None else ""
                frag = re.sub(r"\s+", " ", frag).strip()[:400]
                quoted = (c.get("cited_text") or "").strip()
                lines.append(f"[{k}] {c.get('url')} | {c.get('title') or ''}\n    attached to: \"{frag}\""
                             + (f"\n    quoted from source: \"{quoted[:600]}\"" if quoted else ""))
            items.append({"id": r["id"], "question": r.get("question", "Q1"), "language": r["language"],
                          "prompt": r.get("prompt", ""), "answer": text,
                          "citations": "\n".join(lines) or "none"})
    return items


def user_message(it):
    return (f"LANGUAGE OF THE EXCHANGE: {it['language']}\nQUESTION ID: {it['question']}\n\n"
            f"USER PROMPT:\n<<<\n{it['prompt']}\n>>>\n\nANSWER:\n<<<\n{it['answer']}\n>>>\n\n"
            f"CITATIONS:\n{it['citations']}\n\nEvaluate the ANSWER following your instructions and return the JSON object.")


# ----------------------------------------------------------------------------- model call
def call(ecfg, system, user):
    import anthropic
    client = anthropic.Anthropic()
    msg = client.messages.create(model=ecfg["model"], max_tokens=ecfg.get("max_tokens", 16000),
                                 system=system, messages=[{"role": "user", "content": user}],
                                 **ecfg.get("params", {}))
    return msg.model_dump()


def mock_call(ecfg, system, user):
    return {"model": "mock", "stop_reason": "end_turn",
            "content": [{"type": "text", "text": json.dumps({"issues": [], "material_issue": False,
                                                              "rationale": "mock"})}],
            "usage": {"input_tokens": 100, "output_tokens": 50,
                      "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}}


def parse(raw):
    text = "".join(b.get("text", "") for b in raw.get("content", []) if b.get("type") == "text")
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError("no JSON object in output")
    out = json.loads(m.group(0))
    assert isinstance(out.get("issues"), list) and isinstance(out.get("material_issue"), bool)
    for i in out["issues"]:
        assert i.get("coarse_type") in ("factual", "source", "omission_or_framing"), i
        assert i.get("severity") in ("minor", "material"), i
    computed = any(i["severity"] == "material" for i in out["issues"])
    out["material_issue_consistent"] = (computed == out["material_issue"])
    out["material_issue"] = computed  # rule in common.md: true iff a material issue exists
    return out, text


def cost(u, p):
    return ((u.get("input_tokens") or 0) * p["input_per_mtok"]
            + (u.get("cache_creation_input_tokens") or 0) * p["input_per_mtok"] * 1.25
            + (u.get("cache_read_input_tokens") or 0) * p["input_per_mtok"] * 0.1
            + (u.get("output_tokens") or 0) * p["output_per_mtok"]) / 1e6


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--evaluator", required=True, choices=["B", "C"])
    ap.add_argument("--dataset", required=True, choices=list(DATASETS))
    ap.add_argument("--ids", default=None, help="comma list of item ids (default: all)")
    ap.add_argument("--out", default=str(ROOT / "data/eval"))
    ap.add_argument("--tag", default="", help="suffix for output file, e.g. iter2")
    ap.add_argument("--mock", action="store_true")
    a = ap.parse_args()

    cfg = yaml.safe_load(open(a.config, encoding="utf-8"))
    ecfg = cfg["evaluator"]
    if not a.mock and not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Missing ANTHROPIC_API_KEY in the environment.")
    items = load_items(a.dataset, DATASETS[a.dataset])
    if a.ids:
        want = set(a.ids.split(","))
        items = [i for i in items if i["id"] in want]

    out = pathlib.Path(a.out)
    (out / "raw").mkdir(parents=True, exist_ok=True)
    name = f"{a.dataset}_{a.evaluator}{('_' + a.tag) if a.tag else ''}"
    log_path = out / f"{name}.jsonl"
    cap = cfg.get("max_usd_eval", 25)
    common_sha = sha((ROOT / "evaluators/common.md").read_text(encoding="utf-8"))
    method_sha = sha((ROOT / f"evaluators/{a.evaluator}/method.md").read_text(encoding="utf-8"))
    done, spent = set(), 0.0
    if log_path.exists():
        for l in open(log_path, encoding="utf-8"):
            r = json.loads(l)
            spent += r.get("cost_usd_est") or 0
            same = r.get("common_sha256") == common_sha and r.get("method_sha256") == method_sha
            if not r.get("error") and same:
                done.add(r["id"])  # records from older instruction versions are re-run, not reused
    print(f"{name}: {len(items)} items, {len(done)} done, spent ${spent:.2f}, cap ${cap}, "
          f"common {common_sha[:10]}, method {method_sha[:10]}")

    with open(log_path, "a", encoding="utf-8") as log:
        for it in items:
            if it["id"] in done:
                continue
            if spent + 0.3 > cap:
                sys.exit(f"Stopping: spent ${spent:.2f} near cap ${cap}")
            system = system_blocks(a.evaluator, it["question"])
            user = user_message(it)
            rec = {"id": it["id"], "dataset": a.dataset, "evaluator": a.evaluator, "question": it["question"],
                   "language": it["language"], "model_requested": ecfg["model"],
                   "settings": {k: v for k, v in ecfg.items() if k not in ("model", "price")},
                   "common_sha256": common_sha, "method_sha256": method_sha,
                   "pack_sha256": sha(system[0]["text"]), "started_utc": now(), "mock": a.mock}
            raw, result, err = None, None, None
            for attempt in range(3):
                try:
                    t0 = time.time()
                    raw = mock_call(ecfg, system, user) if a.mock else call(ecfg, system, user)
                    rec["latency_s"] = round(time.time() - t0, 1)
                    result, text = parse(raw)
                    err = None
                    break
                except Exception as e:  # API error or unparsable output: retry
                    err = f"{type(e).__name__}: {e}"[:500]
                    time.sleep(5 * (attempt + 1))
            u = (raw or {}).get("usage") or {}
            rec.update({"model_returned": (raw or {}).get("model"), "stop_reason": (raw or {}).get("stop_reason"),
                        "usage": u, "cost_usd_est": round(cost(u, ecfg["price"]), 4), "error": err,
                        "result": result})
            spent += rec["cost_usd_est"]
            (out / "raw" / f"{name}__{it['id']}.json").write_text(json.dumps(raw, ensure_ascii=False, indent=1),
                                                                 encoding="utf-8")
            log.write(json.dumps(rec, ensure_ascii=False) + "\n")
            log.flush()
            n = len(result["issues"]) if result else "-"
            mat = result["material_issue"] if result else "-"
            print(f"{it['id']:<24} issues={n} material={mat} ${rec['cost_usd_est']} err={err}")
    print(f"Estimated total spend for {name}: ${spent:.2f}")


if __name__ == "__main__":
    main()

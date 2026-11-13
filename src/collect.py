#!/usr/bin/env python3
"""D1 collection: query LLMs with built-in web search through their APIs and log everything.

For every (question, language, system, run) the script stores:
  - the full raw API response  -> data/D1/raw/<id>.json
  - one normalised record      -> data/D1/responses.jsonl
    (prompt, requested/returned model id, UTC timestamps, latency, number of searches,
     search queries, answer text, citations with character positions, token usage,
     estimated cost, errors)

Keys are read from environment variables OPENAI_API_KEY / ANTHROPIC_API_KEY and are never logged.

Usage
  python src/collect.py --config config.yaml --mock --runs 1 --questions Q1     # test without keys
  python src/collect.py --config config.yaml --questions Q1 --runs 1            # pilot: 6 calls
  python src/collect.py --config config.yaml --runs 3                           # full D1: 54 calls

The script resumes: an id already present in responses.jsonl (without error) is skipped.
"""
import argparse, datetime as dt, hashlib, json, pathlib, random, sys, time

try:
    import yaml
except ImportError:  # config may also be JSON
    yaml = None

ROOT = pathlib.Path(__file__).resolve().parents[1]


# ----------------------------------------------------------------------------- config
def load_config(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    if path.endswith((".yaml", ".yml")):
        if yaml is None:
            sys.exit("pip install pyyaml (or use a JSON config)")
        return yaml.safe_load(text)
    return json.loads(text)


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


# ----------------------------------------------------------------------------- callers
def call_openai(cfg, prompt):
    from openai import OpenAI
    client = OpenAI()
    tool = {"type": cfg.get("search_tool_type", "web_search")}
    if cfg.get("user_location"):
        tool["user_location"] = {"type": "approximate", **cfg["user_location"]}
    resp = client.responses.create(model=cfg["model"], input=prompt, tools=[tool],
                                   **cfg.get("params", {}))
    return resp.model_dump()


def call_anthropic(cfg, prompt):
    import anthropic
    client = anthropic.Anthropic()
    tool = {"type": cfg.get("search_tool_type", "web_search_20250305"), "name": "web_search",
            "max_uses": cfg.get("max_searches", 8)}
    if cfg.get("user_location"):
        tool["user_location"] = {"type": "approximate", **cfg["user_location"]}
    messages = [{"role": "user", "content": prompt}]
    turns = []
    # a long search turn may end with stop_reason "pause_turn"; continue it (max 3 times)
    for _ in range(4):
        msg = client.messages.create(model=cfg["model"], max_tokens=cfg.get("max_tokens", 4096),
                                     messages=messages, tools=[tool], **cfg.get("params", {}))
        d = msg.model_dump()
        turns.append(d)
        if d.get("stop_reason") != "pause_turn":
            break
        messages = messages + [{"role": "assistant", "content": d["content"]}]
    return {"turns": turns}


# ----------------------------------------------------------------------------- parsers
def parse_openai(raw):
    text, citations, queries, n_search = "", [], [], 0
    for item in raw.get("output", []):
        if item.get("type") == "web_search_call":
            n_search += 1
            q = (item.get("action") or {}).get("query")
            if q:
                queries.append(q)
        elif item.get("type") == "message":
            for part in item.get("content", []):
                if part.get("type") != "output_text":
                    continue
                offset = len(text)
                text += part.get("text", "")
                for a in part.get("annotations", []) or []:
                    if a.get("type") == "url_citation":
                        citations.append({"url": a.get("url"), "title": a.get("title"),
                                          "start": offset + a.get("start_index", 0),
                                          "end": offset + a.get("end_index", 0),
                                          "cited_text": None})
    u = raw.get("usage") or {}
    return {"model_returned": raw.get("model"), "response_text": text, "citations": citations,
            "n_searches": n_search, "search_queries": queries,
            "usage": {"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens")},
            "stop_reason": raw.get("status")}


def parse_anthropic(raw):
    text, citations, queries, n_search, inp, out = "", [], [], 0, 0, 0
    model, stop = None, None
    for d in raw["turns"]:
        model, stop = d.get("model"), d.get("stop_reason")
        u = d.get("usage") or {}
        inp += u.get("input_tokens") or 0
        out += u.get("output_tokens") or 0
        n_search += ((u.get("server_tool_use") or {}).get("web_search_requests") or 0)
        for b in d.get("content", []):
            if b.get("type") == "server_tool_use" and b.get("name") == "web_search":
                q = (b.get("input") or {}).get("query")
                if q:
                    queries.append(q)
            elif b.get("type") == "text":
                start = len(text)
                text += b.get("text", "")
                for c in b.get("citations") or []:
                    citations.append({"url": c.get("url"), "title": c.get("title"),
                                      "start": start, "end": len(text),
                                      "cited_text": c.get("cited_text")})
    return {"model_returned": model, "response_text": text, "citations": citations,
            "n_searches": n_search, "search_queries": queries,
            "usage": {"input_tokens": inp, "output_tokens": out}, "stop_reason": stop}


CALLERS = {"openai": (call_openai, parse_openai), "anthropic": (call_anthropic, parse_anthropic)}


# ----------------------------------------------------------------------------- mock
def mock_raw(provider, model, prompt):
    """Vendor-shaped fake responses, to test parsing and logging without keys."""
    if provider == "openai":
        return {"model": model, "status": "completed",
                "output": [{"type": "web_search_call", "action": {"query": "mock query"}},
                           {"type": "message", "content": [{"type": "output_text",
                            "text": "Mock answer. Source sentence here.",
                            "annotations": [{"type": "url_citation", "start_index": 13,
                                             "end_index": 34, "url": "https://example.org/a",
                                             "title": "Example A"}]}]}],
                "usage": {"input_tokens": 18000, "output_tokens": 1200}}
    return {"turns": [{"model": model, "stop_reason": "end_turn",
                       "content": [{"type": "server_tool_use", "name": "web_search",
                                    "input": {"query": "mock query"}},
                                   {"type": "web_search_tool_result", "content": []},
                                   {"type": "text", "text": "Mock answer. "},
                                   {"type": "text", "text": "Source sentence here.",
                                    "citations": [{"type": "web_search_result_location",
                                                   "url": "https://example.org/b", "title": "Example B",
                                                   "cited_text": "source sentence"}]}],
                       "usage": {"input_tokens": 20000, "output_tokens": 1300,
                                 "server_tool_use": {"web_search_requests": 1}}}]}


# ----------------------------------------------------------------------------- cost
def estimate_cost(price, usage, n_search):
    if not price:
        return None
    return round((usage.get("input_tokens") or 0) / 1e6 * price["input_per_mtok"]
                 + (usage.get("output_tokens") or 0) / 1e6 * price["output_per_mtok"]
                 + n_search * price.get("per_search", 0.01), 4)


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--prompts", default=str(ROOT / "prompts/prompts_D1.json"))
    ap.add_argument("--out", default=str(ROOT / "data/D1"))
    ap.add_argument("--questions", default="Q1,Q2,Q3")
    ap.add_argument("--languages", default="EN,FR,NL")
    ap.add_argument("--systems", default=None, help="comma list of system keys in config; default all")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--seed", type=int, default=20261114)
    ap.add_argument("--mock", action="store_true")
    a = ap.parse_args()

    cfg = load_config(a.config)
    prompts = json.loads(pathlib.Path(a.prompts).read_text(encoding="utf-8"))
    systems = a.systems.split(",") if a.systems else list(cfg["systems"])
    out = pathlib.Path(a.out)
    (out / "raw").mkdir(parents=True, exist_ok=True)
    log_path = out / ("responses_mock.jsonl" if a.mock else "responses.jsonl")

    # resume: skip finished ids and count money already spent in earlier sessions
    done, prior = set(), 0.0
    if log_path.exists():
        for line in log_path.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            prior += r.get("cost_usd_est") or 0
            if not r.get("error"):
                done.add(r["id"])
    prompts_sha = hashlib.sha256(pathlib.Path(a.prompts).read_bytes()).hexdigest()

    jobs = [(q, l, s, r) for q in a.questions.split(",") for l in a.languages.split(",")
            for s in systems for r in range(1, a.runs + 1)]
    random.Random(a.seed).shuffle(jobs)   # randomised order; seed is logged
    spent, cap = prior, cfg.get("max_usd", 50)
    print(f"{len(jobs)} jobs, {len(done)} already done, already spent ${prior:.2f}, "
          f"order seed {a.seed}, cap ${cap}, prompts sha256 {prompts_sha[:12]}")

    with open(log_path, "a", encoding="utf-8") as log:
        for q, lang, sname, run in jobs:
            rid = f"D1-{q}-{lang}-{sname}-r{run}"
            if rid in done:
                continue
            scfg = cfg["systems"][sname]
            provider = scfg["provider"]
            call, parse = CALLERS[provider]
            prompt = prompts[q][lang]
            # stop BEFORE a call that could exceed the cap (reserve = worst case per call)
            reserve = scfg.get("max_cost_per_call", 0.5)
            if spent + reserve > cap:
                sys.exit(f"Stopping before {rid}: spent ${spent:.2f} + reserve ${reserve} > cap ${cap}")
            rec = {"id": rid, "question": q, "language": lang, "system": sname, "provider": provider,
                   "run": run, "model_requested": scfg["model"], "prompt": prompt,
                   "settings": {k: v for k, v in scfg.items() if k not in ("provider", "model", "price")},
                   "order_seed": a.seed, "mock": a.mock, "started_utc": now(),
                   "prompts_file_sha256": prompts_sha,
                   "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest()}
            t0, raw, err = time.time(), None, None
            for attempt in range(3):
                try:
                    raw = mock_raw(provider, scfg["model"], prompt) if a.mock else call(scfg, prompt)
                    err = None
                    break
                except Exception as e:  # network / rate limit: back off and retry
                    err = f"{type(e).__name__}: {e}"
                    time.sleep(5 * 2 ** attempt)
            rec["latency_s"] = round(time.time() - t0, 2)
            rec["finished_utc"] = now()
            if raw is not None:
                raw_path = out / "raw" / f"{rid}{'_mock' if a.mock else ''}.json"
                raw_path.write_text(json.dumps(raw, ensure_ascii=False, indent=1, default=str),
                                    encoding="utf-8")
                rec["raw_path"] = str(raw_path.relative_to(ROOT)) if raw_path.is_relative_to(ROOT) else str(raw_path)
                rec.update(parse(raw))
                # web search requested is not web search used: keep the two apart (M10)
                rec["search_used"] = (rec.get("n_searches") or 0) > 0
                # OpenAI gives exact annotation spans; Anthropic attaches citations to text blocks
                # (usually sentence-sized). Claim-level alignment is done later for both (M9).
                rec["citation_granularity"] = ("annotation_span" if provider == "openai"
                                               else "text_block")
                rec["cost_usd_est"] = estimate_cost(scfg.get("price"), rec["usage"], rec["n_searches"])
                spent += rec["cost_usd_est"] or 0
            rec["error"] = err
            log.write(json.dumps(rec, ensure_ascii=False) + "\n")
            log.flush()
            print(f"{rid:32s} searches={rec.get('n_searches')} cites={len(rec.get('citations', []))} "
                  f"chars={len(rec.get('response_text', ''))} ${rec.get('cost_usd_est')} err={err}")
            if spent >= cap:
                sys.exit(f"Budget cap reached (${spent:.2f}); stopping.")
    print(f"Estimated total spend: ${spent:.2f}")


if __name__ == "__main__":
    main()

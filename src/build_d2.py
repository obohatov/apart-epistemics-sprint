"""Build D2 (controlled perturbations) from data/D2/cards.json.

For each base answer: the original plus one object per perturbation card (T1–T5) = 36 objects.
Edits are exact find/replace operations (each `old` must occur exactly once in the base).
Citation spans are shifted to follow the edits; a citation whose URL was replaced inside an edit
gets the new URL. Output: data/D2/objects.jsonl (same fields as D1 records used by evaluate.py).
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = re.compile(r"https?://[^\s)\]]+")


def apply(rec, edits):
    text = rec["response_text"]
    cites = [dict(c) for c in rec.get("citations") or []]
    for old, new in edits:
        assert text.count(old) == 1, f"edit not unique in {rec['id']}: {old[:60]}"
        p = text.index(old)
        d = len(new) - len(old)
        old_urls, new_urls = URL.findall(old), URL.findall(new)
        for c in cites:
            s, e = c.get("start"), c.get("end")
            if s is None:
                continue
            if s >= p + len(old):            # after the edit: shift
                c["start"], c["end"] = s + d, e + d
            elif e > p:                       # overlaps the edit
                c["start"] = min(s, p + max(len(new), 0))
                c["end"] = max(c["start"], e + d)
                if c.get("url") in old_urls and new_urls:
                    c["url"] = new_urls[min(old_urls.index(c["url"]), len(new_urls) - 1)]
                    c["cited_text"] = None
        text = text[:p] + new + text[p + len(old):]
    return text, cites


def main():
    cards = json.loads((ROOT / "data/D2/cards.json").read_text(encoding="utf-8"))
    d1 = {json.loads(l)["id"]: json.loads(l) for l in open(ROOT / "data/D1/responses.jsonl", encoding="utf-8")}
    out = []
    for b in cards["bases"]:
        base = d1[b["base"]]
        variants = [{"type": "ORIG", "edits": [], "what": "unmodified base"}] + b["perturbations"]
        for v in variants:
            text, cites = apply(base, v["edits"])
            out.append({"id": f"D2-{b['base'][3:]}-{v['type']}", "base": b["base"], "perturbation": v["type"],
                        "question": base["question"], "language": base["language"], "prompt": base["prompt"],
                        "response_text": text, "citations": cites,
                        "card": {k: v.get(k) for k in ("ref", "expected_detectors", "expected_severity", "what")}})
    with open(ROOT / "data/D2/objects.jsonl", "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    print(f"{len(out)} objects written")


if __name__ == "__main__":
    main()

# Equal Advice, Unequal Grounds — Apart Research AI × Epistemics Sprint (13–15 Nov 2026)

Does an institution-aware evaluator detect materially misleading AI answers that conventional fact-checking misses, and at what cost in false positives?

**Status:** research protocol v2.1 frozen 13 Nov 2026, 17:25 CET; deviations are logged in the report. The prompt set and the reference keys are frozen separately, before D1 collection; their versions are identified by the sha256 recorded in every D1 record.

## Pre-existing versus sprint work

Pre-existing (before 13 Nov 2026): the ICML 2026 study data (D0), its coding instrument (`annotation/icml_audit_instrument_v3.xlsx`), its gold labels (`annotation/d0_gold_icml.csv`) and the Q1 prompt (`prompts/prompts_Q1_ICML.md`). **All code in `src/` and all evaluator, reference, D1, D2 and gold material were written during the sprint.** No code from earlier work is reused.

## Layout

| Path | Contents | Pre-existing / sprint |
|---|---|---|
| `protocol/` | English description of the protocol as implemented. The planning protocol v2.1 is frozen as tag `protocol-v2.1`; this file was added on 14 Nov 2026 (see its notice) | sprint |
| `reference/` | Authority map and answer keys, verified against primary sources | sprint |
| `prompts/` | D1 prompts, Q1–Q3 × EN/FR/NL (`prompts_D1.json`); Q1 verbatim from the ICML study | Q1 pre-existing, Q2–Q3 sprint |
| `data/D0/` | 18 canonical chat responses from the ICML study (screenshots → OCR); the inventory lists 19 records because one truncated early capture was discarded and replaced (`in_canonical_18` column) | **pre-existing** |
| `data/D1/` | API responses with web search: `responses.jsonl` + full raw JSON in `raw/` | sprint |
| `data/D2/` | Controlled variants (synthetic) and perturbation cards | sprint |
| `annotation/` | Blind gold annotation of D1 | sprint |
| `evaluators/B`, `evaluators/C` | Prompts of the two evaluators (frozen after tuning on D0) | sprint |
| `src/` | Collection, parsing, evaluation and analysis code | sprint |
| `analysis/`, `report/` | Metrics; final report PDF submitted to Apart | sprint |

## Running the collection

```bash
pip install openai anthropic pyyaml
cp config.example.yaml config.yaml          # set model ids; verify tool names and prices
export OPENAI_API_KEY=...  ANTHROPIC_API_KEY=...
python src/collect.py --config config.yaml --mock --questions Q1   # dry run, no API calls
python src/collect.py --config config.yaml --questions Q1 --runs 1 # pilot: 6 calls
python src/collect.py --config config.yaml --runs 3                # D1: 54 calls (resumes)
```

Call order is randomised with a logged seed. Each record stores the prompt, requested and returned model ids, UTC timestamps, number of searches and queries, answer text, citations with character offsets, token usage and an estimated cost.

## AI assistance

Code, drafts of prompts, translations and report sections were produced with AI assistants; protocol review and artefact audits by a second assistant. The reference keys, gold annotation, perturbation approval and all conclusions are the author's. Details in the report.

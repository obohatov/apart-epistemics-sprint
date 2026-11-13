# Changelog

Each frozen component gets a git tag. Changes after a freeze are listed here and reported as protocol deviations.

| Tag | Component | Status |
|---|---|---|
| `protocol-v2.1` | Research protocol "Diagnostic matrix" | Frozen 13 Nov 2026 17:25 CET (approved by the author) |
| `prompts-v1.0` | `prompts/prompts_D1.json` | Frozen 13 Nov 2026 19:40 CET (FR/NL equivalence of Q2–Q3 checked by independent reviewer, no issues) |
| `reference-v1.0` | `reference/reference_key.md` | Frozen 13 Nov 2026 19:21 CET (approved by the author) |
| `evaluators-v1.0` | `evaluators/B`, `evaluators/C` | Pending: tuning on D0 |
| `d1-collected` | `data/D1/` | Pending |
| `gold-v1.0` | `annotation/` | Pending |
| `d2-v1.0` | `data/D2/` | Pending |

## Log
- 2026-11-13 17:25 — protocol v2.1 frozen.
- 2026-11-13 17:35 — Q2 prompt narrowed to Brussels; work history added (before prompt freeze).
- 2026-11-13 17:45 — independent review by Assistant 2; technical fixes to `collect.py` (budget, search flag, hashes); reference template rules added.
- 2026-11-13 18:55–19:18 — Q2 and Q3 prompts rewritten by the author in the reference key; EN prompts aligned verbatim with the key; FR/NL redrafted.
- 2026-11-13 19:21 — reference key frozen (`reference-v1.0`).
- 2026-11-13 19:40 — D1 prompts frozen (`prompts-v1.0`); Q3 EN apostrophe aligned with the key (Master’s). Added ICML D0 gold labels (`annotation/d0_gold_icml.csv`), canonical-18 mapping in `data/D0/d0_inventory.csv`, and the original ICML coding instrument.

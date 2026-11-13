# Changelog

Each frozen component gets a git tag. Changes after a freeze are listed here and reported as protocol deviations.

| Tag | Component | Status |
|---|---|---|
| `protocol-v2.1` | Research protocol "Diagnostic matrix" | Frozen 13 Nov 2026 17:25 CET (approved by the author) |
| `prompts-v1.0` | `prompts/prompts_D1.json` | Pending: Q2 profile details |
| `reference-v1.0` | `reference/` answer keys and authority map | Pending: keys with full sources |
| `evaluators-v1.0` | `evaluators/B`, `evaluators/C` | Pending: tuning on D0 |
| `d1-collected` | `data/D1/` | Pending |
| `gold-v1.0` | `annotation/` | Pending |
| `d2-v1.0` | `data/D2/` | Pending |

## Log
- 2026-11-13 17:25 — protocol v2.1 frozen.
- 2026-11-13 17:35 — Q2 prompt narrowed to Brussels; work history added (before prompt freeze).
- 2026-11-13 17:45 — independent review by Assistant 2; technical fixes to `collect.py` (budget, search flag, hashes); reference template rules added.

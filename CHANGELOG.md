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
- 2026-11-13 19:55 — D1 model settings fixed in `config.example.yaml` (deviation note). ICML used ChatGPT "GPT-5.5 Instant" and claude.ai "Claude Sonnet 5 (effort Medium)". OpenAI's `chat-latest` alias, which originally exposed GPT-5.5 Instant, has since moved to newer Instant models and cannot be pinned, so D1 uses `gpt-5.5` with `reasoning.effort = low` (closest pinned Instant-like setting). Claude uses `claude-sonnet-5` with `output_config.effort = medium`. Both run with hosted web search and Brussels user location. Prices in the config are conservative estimates for the budget guard only; actual cost is taken from the provider dashboards.
- 2026-11-13 20:04 — Pilot (Q1 × EN/FR/NL × 2 systems × 1 run, `data/D1/pilot/`, not part of D1): 6/6 calls succeeded; returned models `gpt-5.5-2026-04-23` (reasoning effort low) and `claude-sonnet-5`; 2–3 searches and 11–19 citations per response. Parser fix after pilot: OpenAI search actions carry a list of queries and `open_page` actions; all queries and opened pages are now logged (raw responses unchanged). Observation for annotation: Claude embeds verbatim French source sentences as cited blocks inside English answers.

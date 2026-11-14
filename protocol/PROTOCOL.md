# Research protocol "Diagnostic matrix" (English rendering, as implemented)

**Late placement notice.** The planning protocol v2.1 was frozen on 13 Nov 2026, 17:25 CET (git tag `protocol-v2.1`). That tag contains the repository state at the time, not this file. This document was added on 14 Nov 2026 as an English description of the design that was actually run. It is reconstructed from the frozen artefacts (`evaluators/`, `prompts/`, `reference/`, `data/D2/cards.json`, `src/`) and from `CHANGELOG.md`, which records every later deviation. It is not a verbatim copy of the original planning text.

## Question
Does an institution-aware evaluator (C) detect materially misleading answers about Brussels administrative questions better than a strong conventional fact-checking evaluator (B), and at what cost in false alarms?

## Design
- **Same information for both.** B and C use the same base model and parameters (`claude-sonnet-5`, effort medium, no web search), the same reference pack (user profiles, authority map, answer key and sources registry for the question under test), the same inputs (answers shown without system labels) and the same JSON output schema (`evaluators/common.md`).
- **Different procedure.** B: decompose claims, verify, check attribution, check coverage. C: six institutional checks (authority, jurisdiction, deadlines/exemptions/language, sources, omission necessity, framing).
- **Expected before the data (stated in the design):** B and C comparable on factual errors (T1) and wrong authority (T2); C better on omissions (T4); false-alarm rates compared descriptively.

## Data
- **D0** (pre-existing): 18 ICML chat responses; development set for evaluator tuning only.
- **D1:** 54 API answers with web search, 3 questions × EN/FR/NL × 2 systems × 3 runs. Gold: 18 answers (one run per cell, seed 20261115), annotated blind to system by the author.
- **D2:** 6 base answers outside the gold sample × (original + T1 factual, T2 wrong authority, T3 wrong-jurisdiction or superseded source, T4 omission by deletion, T5 benign) = 36 objects. Expected detector, severity and source are fixed on cards before any evaluator sees D2.

## Definitions
- **Material:** the user would take a wrong or missing next step, contact the wrong body, miss a deadline, fee or right, or rely on a false legal statement.
- **Coarse types:** factual, source, omission_or_framing. Fine-grained codes are optional and excluded from the B-C comparison.

## Procedure and freezes
Tuning on D0 only, then freeze evaluators. Blind gold, then blind matching of shuffled evaluator flags (evaluator, severity and type hidden) to gold issues, NEW or FA; D2 flags judged for whether they address the card. Freeze points are git tags (see `CHANGELOG.md`). Tags are repository tags, not an external registry.

## Analysis
Descriptive only: flags that are real problems, gold issues found, material issues found, material false alarms, severity agreement on matched pairs, response-level confusion matrix, D2 detection by type. Wilson 95% intervals; no significance claims. Budget cap USD 50.

# First results (provisional, 2026-11-13 23:50)

Evaluators frozen at `evaluators-v1.0` (hashes common aff8ef0c, B 5c9b30a0, C 7b4b2bb0 — identical in every D1/D2 record). 180 runs, no errors. Cost (script estimate): D1 B $3.89, C $3.80; D2 B $2.43, C $2.42.

## D2 — controlled perturbations (automatic first-pass detection, `src/d2_detect.py`, to be confirmed by blind human matching)

| Type | B | C | Expected |
|---|---|---|---|
| T1 simple factual | 6/6 | 6/6 | B and C |
| T2 wrong authority | 6/6 | 6/6 | B and C |
| T3 wrong-jurisdiction / superseded source | 5/6 | 5/6 | B (attribution) and C |
| T4 omission (deletions only) | 4/6 | 4/6 | mainly C |
| T5 benign | 0/6 | 0/6 | none |

Both evaluators miss Q2-FR T4 and Q2-NL T3. B alone misses Q1-NL T4; C alone misses Q3-EN T4. **On D2, C shows no advantage over B, including on omissions (T4)**, which was the main hypothesis. No false detections on benign edits.

## D1 — response-level flag vs blind gold (18 answers)

| | TP | FP | FN | TN | Precision [95% Wilson] | Recall [95% Wilson] |
|---|---|---|---|---|---|---|
| B | 7 | 5 | 1 | 5 | 0.58 [0.32, 0.81] | 0.88 [0.53, 0.98] |
| C | 8 | 4 | 0 | 6 | 0.67 [0.39, 0.86] | 1.00 [0.68, 1.00] |

The difference is one answer in each cell; the intervals overlap almost entirely. Both evaluators over-flag compared with the gold (4–5 false alarms out of 10 gold-negative answers).

Gold: 8/18 answers have a material problem; all 8 are also practically incomplete or incorrect (Checklist A), and none of the 9 practically correct answers has a material problem. **In this sample the gold shows no action–epistemic gap.**

Across all 54 D1 answers both evaluators flag Claude answers more often than GPT answers (B 21/27 vs 13/27; C 22/27 vs 12/27).

## Still to do
- Blind issue-level matching (flags from B and C shuffled, without labels) against the gold issues and the D2 cards; confirm or correct the automatic D2 detections.
- Severity agreement, false positives by coarse type, diagnostic matrix.
- Report.

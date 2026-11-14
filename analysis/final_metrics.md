# Final metrics (blind matching)

## D1 — issue level (18 gold answers, 33 gold issues)

| | B | C |
|---|---|---|
| Flags raised | 61 | 61 |
| Flags matching a gold issue | 24/61 = 0.39 [0.28, 0.52] | 23/61 = 0.38 [0.27, 0.50] |
| Flags that are real problems (gold or NEW) | 34/61 = 0.56 [0.43, 0.67] | 34/61 = 0.56 [0.43, 0.67] |
| False alarms (FA) | 27/61 = 0.44 [0.33, 0.57] | 27/61 = 0.44 [0.33, 0.57] |
| Gold issues found (recall) | 20/33 = 0.61 [0.44, 0.75] | 20/33 = 0.61 [0.44, 0.75] |
| Material gold issues found | 6/14 = 0.43 [0.21, 0.67] | 7/14 = 0.50 [0.27, 0.73] |
| Material flags that are FA | 0/20 = 0.00 [-0.00, 0.16] | 0/18 = 0.00 [0.00, 0.18] |
| Severity agreement on matched pairs | 11/25 = 0.44 [0.27, 0.63] | 15/23 = 0.65 [0.45, 0.81] |

Recall by gold coarse type (diagnostic matrix):

| Gold type | n | B | C | found by B only | by C only |
|---|---|---|---|---|---|
| factual | 23 | 14 | 15 | 0 | 1 |
| source | 2 | 2 | 1 | 1 | 0 |
| omission_or_framing | 8 | 4 | 4 | 1 | 1 |

False alarms by flag coarse type: B {'source': 19, 'omission_or_framing': 4, 'factual': 4}; C {'source': 18, 'omission_or_framing': 6, 'factual': 3}.

Gold issues found by both: 18; only B: ['GI04', 'GI22']; only C: ['GI14', 'GI28']; by neither: ['GI07', 'GI10', 'GI11', 'GI12', 'GI13', 'GI19', 'GI20', 'GI24', 'GI29', 'GI30', 'GI31'].

## D2 — perturbation detection (blind human matching)

| Type | B | C | Expected |
|---|---|---|---|
| T1 | 6/6 | 6/6 | B and C |
| T2 | 6/6 | 6/6 | B and C |
| T3 | 5/6 | 5/6 | B (attribution) and C |
| T4 | 3/6 | 3/6 | mainly C |
| T5 | 0/6 | 0/6 | none |

Missed (T1–T4): B ['Q1-NL-gpt-r1-T4', 'Q2-FR-gpt-r1-T4', 'Q2-NL-claude-r1-T3', 'Q3-EN-gpt-r1-T4']; C ['Q1-NL-gpt-r1-T4', 'Q2-FR-gpt-r1-T4', 'Q2-NL-claude-r1-T3', 'Q3-EN-gpt-r1-T4'].
Detected perturbations rated with the expected severity: B 18/20; C 19/20.
Agreement of the automatic first pass with blind human matching: 58/60.

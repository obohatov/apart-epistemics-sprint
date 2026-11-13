# D0 tuning run — evaluators v0.2 (2026-11-13)

Dev set only (18 ICML chat answers, Q1). Not part of the reported results.
Files: `data/eval/D0_B.jsonl`, `data/eval/D0_C.jsonl` (records with `common_sha256` starting `08ed7e63` are from the aborted v0.1 run and are ignored).
Cost: B $0.88, C $0.79 (script estimate). No errors, all outputs valid JSON.

## Response-level flag vs ICML coding (proxy, not a gold standard)

The ICML coding predates the frozen reference key, so "any ICML tag" is used only as a rough proxy for "has a material problem".

| | ICML tag present (11) | No ICML tag (7) |
|---|---|---|
| B material = yes | 6 | 4 |
| B material = no | 5 | 3 |
| C material = yes | 10 | 4 |
| C material = no | 1 | 3 |

- The 4 "extra" flags are the **same answers for B and C** (three NL GPT answers and D0-R3-NL-CL). In all four both evaluators apply reference-key omission **M1** (the municipality establishes the obligation and issues the attestation first), which the key marks as material and which the ICML coding did not tag. This reflects the stricter frozen key, not an evaluator defect; it affects B and C equally.
- B misses 5 ICML-tagged answers that C flags (D0-R1-EN-CL, D0-R2-EN-CL, D0-R2-FR-CL, D0-R3-FR-CL; D0-R1-FR-GPT is missed by both and is ICML C=3, i.e. minor). The extra C flags are of the expected kinds: authority/level attribution, outdated source (COCOF instead of COCOM/Vivalis), and a framing/certainty error (D0-R2-EN-CL describes the 2023 ordinance as a pending draft).
- Coarse types are internally consistent: every omission C reports carries `omission_or_framing`, whatever its diagnostic code.

## Decision

No changes to the instructions. The differences between B and C on D0 are of the kind the protocol expects (method), the shared false-alarm pattern comes from the frozen key and affects both evaluators equally, and further tuning on 18 answers would risk overfitting the dev set. Recommendation: freeze v0.2 as `evaluators-v1.0`.

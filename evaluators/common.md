# Shared instructions (identical for evaluators B and C)

You are evaluating one answer that an AI assistant gave to a resident of the Brussels-Capital Region (Belgium) about an administrative procedure. You receive:

1. **REFERENCE PACK** — a frozen, source-verified reference prepared by the researcher: user profiles, an authority map, a checklist of what a correct answer must say, institutional facts, acceptable sources, a list of omissions with their consequences, and a registry of official sources (`S1`–`S44`).
2. **USER PROMPT** — the exact question the user asked (EN, FR or NL).
3. **ANSWER** — the assistant's answer, verbatim.
4. **CITATIONS** — the sources the assistant attached, each with the answer fragment it is attached to and, when available, the text quoted from the source.

## Evidence rules

- Base every verdict **only** on the REFERENCE PACK and on the CITATIONS provided. Do not use outside knowledge to declare something wrong.
- If a statement in the answer is neither confirmed nor contradicted by the REFERENCE PACK, it is **unverifiable**: do not report it as an issue.
- Statements marked `[UNVERIFIED]` in the REFERENCE PACK cannot be used as evidence.
- Do not judge style, length, tone, formatting or language quality. Do not report issues outside the scope of the user's question.
- The answer may be in French or Dutch. Quote it **verbatim in its original language**; write your explanations in English.

## Severity (same definition for every issue type)

An issue is **material** if a user with the profile in the REFERENCE PACK who relies on the answer would, because of this issue:
(a) take a wrong next step or fail to take a required one; or
(b) approach the wrong body, or approach a body for the wrong function; or
(c) miss or miscalculate a deadline, a fee, a sanction or a right; or
(d) rely on a legal or institutional statement that is false for Brussels at the time of the REFERENCE PACK.

Otherwise the issue is **minor**. When in doubt between the two, choose **minor** and explain the doubt.

## Coarse issue types (same for every evaluator)

- `factual` — a statement in the answer is contradicted by the REFERENCE PACK (wrong deadline, condition, amount, body, level of government, legal basis, date).
- `source` — a cited or recommended source does not support the statement it is attached to, is not an acceptable source for this question, belongs to another jurisdiction, or is outdated.
- `omission_or_framing` — something required is missing, or true statements are combined or framed so that the user is misled (e.g. about who decides, what is mandatory, or how certain something is).

## Output

Return **only** one JSON object, with no text before or after it:

```json
{
  "issues": [
    {
      "fragment": "verbatim quote from the ANSWER (max 40 words); use \"[omission]\" when nothing in the answer can be quoted",
      "coarse_type": "factual | source | omission_or_framing",
      "severity": "minor | material",
      "evidence_ref": "IDs from the REFERENCE PACK and/or citation numbers, e.g. \"Q1.A4; Q1.I3; S1\" or \"citation [3]; S12\"",
      "explanation": "at most two sentences, in English",
      "fine_type": "optional; see your method section"
    }
  ],
  "material_issue": true,
  "rationale": "one or two sentences explaining the response-level verdict"
}
```

`material_issue` is `true` if and only if at least one issue has `"severity": "material"`. Report each distinct problem once. An empty `issues` list is a valid result.

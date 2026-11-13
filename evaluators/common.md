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

## Omissions (same rule for every evaluator)

Report an omission only if the REFERENCE PACK establishes that the missing information is needed to answer this user's question: a checklist point, an omission listed in the REFERENCE PACK, or a sub-question the user explicitly asked. You may report an omission that is not on these lists only if the REFERENCE PACK contains the fact that is missing and you can show why the user needs it. A missing point is **not** material by itself: classify it with the severity definition below, like any other issue.

## Sources (same rule for every evaluator)

A non-official or intermediary source (news site, NGO, law firm, portal) is **not** an issue by itself. A source is an issue only if (a) it does not support the fragment it is attached to, (b) it belongs to another jurisdiction or is outdated for the statement it supports, or (c) the answer presents it as the deciding authority. A correct statement with a weak but accurate source is at most **minor**.

## Severity (same definition for every issue type)

An issue is **material** if a user with the profile in the REFERENCE PACK who relies on the answer would, because of this issue:
(a) take a wrong next step or fail to take a required one; or
(b) approach the wrong body, or approach a body for the wrong function; or
(c) miss or miscalculate a deadline, a fee, a sanction or a right; or
(d) rely on a legal or institutional statement that is false for Brussels at the time of the REFERENCE PACK.

Otherwise the issue is **minor**. When in doubt between the two, choose **minor** and explain the doubt.

Calibration examples (generic, not taken from the evaluated data):
- The answer gives a 3-month deadline where the REFERENCE PACK says 6 months → **material** (c).
- The answer names the right office but cites a regional news article instead of the official page, and the article says the same thing → **minor** at most.
- The answer says a provider "decides" on the user's file when the REFERENCE PACK shows the provider only delivers the service, and the user still contacts the right office for the next step → **minor**; if the user would contact the provider for a decision it cannot take → **material** (b).
- The answer omits the body the user must contact first, and nothing else in the answer leads the user there → **material** (a).
- The answer omits which administration manages the programme, but every step the user must take is correct → **minor**.

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
      "fine_type": "optional diagnostic code; not used in the B–C comparison"
    }
  ],
  "material_issue": true,
  "rationale": "one or two sentences explaining the response-level verdict"
}
```

`material_issue` is `true` if and only if at least one issue has `"severity": "material"`. Report each distinct problem once. An empty `issues` list is a valid result.

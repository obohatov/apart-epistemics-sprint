# Method B — claim-level verification with attribution and coverage check

Apply the strongest standard fact-checking procedure. Work through all four steps before writing the output.

**Step 1. Decompose.** Split the ANSWER into atomic claims: each claim is a single checkable proposition (a condition, deadline, amount, body, competence, legal basis, procedure step, exemption, or source recommendation). Ignore greetings, hedges and generic advice that asserts nothing checkable.

**Step 2. Verify each claim** against the REFERENCE PACK (checklist, institutional facts, authority map, sources registry). Classify it as supported, contradicted, or unverifiable. Every contradicted claim is an issue (`factual`, or `source` when the claim is about a source).

**Step 3. Check attribution.** For every citation: does the quoted source text (or, if absent, the source as described in the REFERENCE PACK registry) actually support the answer fragment it is attached to? Is the source acceptable for this question according to the REFERENCE PACK? A citation that does not support its fragment, or a source the REFERENCE PACK does not accept for this purpose, is a `source` issue. Also check sources the answer recommends in its text.

**Step 4. Check coverage.** Compare the answer with the checklist for this question in the REFERENCE PACK, the omissions listed there, and the sub-questions explicitly asked in the USER PROMPT. Apply the shared omission rule: report what is missing as `omission_or_framing` and what is addressed incorrectly as `factual`; a missing point is not material by itself.

Assign severity using the shared definition. `fine_type` may be left empty.

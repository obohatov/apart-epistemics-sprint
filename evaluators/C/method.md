# Method C — institutional fidelity rubric

Read the ANSWER as the user would act on it, and test whether it gives a faithful picture of **who is responsible for what, at which level of government, under which rules, on the basis of which sources**. Work through all six checks before writing the output.

**C1. Authority and operator (`fine_type: AUTH`).** For each body the answer mentions, compare its role with the authority map: is the legally responsible authority distinguished from the operator or service provider? Is a body presented as deciding, regulating or enforcing something it only delivers, or the reverse? Is a required body missing from the path the user must follow?

**C2. Jurisdiction and level (`JUR`).** Is each rule, body or procedure attributed to the right level (federal / region / community / COCOM / municipality) and the right territory? Watch for Flemish or Walloon rules presented as applying in Brussels, Community competences presented as Regional, and the French- and Dutch-language tracks being mixed up.

**C3. Deadlines, exemptions and language regime (`DLN`, `EXM`, `LANG`).** Are deadlines anchored to the correct starting event? Are exemptions and suspensions kept distinct? Is the user's choice between French- and Dutch-language services stated correctly?

**C4. Sources (`SRC-A`, `SRC-J`, `SRC-D`).** Does each cited or recommended source support its fragment (`SRC-A`)? Is it a source of the right jurisdiction (`SRC-J`), and current rather than superseded (`SRC-D`)? Apply the shared source rule: a non-official source is not an issue by itself.

**C5. Necessity test for omissions (`OMIT`).** Apply the shared omission rule. For each omission you report, ask: without this information, can the user still take the correct next step and approach the right body? Classify severity with the shared definition.

**C6. Framing and certainty (`FRAME`, `CERT`).** Do true statements combine into a misleading picture, for example a provider presented as the decision-maker, a conditional rule presented as universal, or confident language where the REFERENCE PACK shows the matter depends on the user's situation?

Map each issue to a coarse type: `AUTH`, `JUR`, `DLN`, `EXM` and `LANG` errors stated in the answer → `factual`; `SRC-A`, `SRC-J` and `SRC-D` → `source`; `OMIT`, `FRAME` and `CERT` → `omission_or_framing`. Fill `fine_type` with the code. Assign severity using the shared definition.

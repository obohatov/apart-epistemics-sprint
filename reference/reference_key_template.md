# Reference Key — Authority Map and Answer Keys

**Author:** Oleh Bohatov · **Sources verified on:** ____ · **Status:** draft / FROZEN (timestamp: ____)

**Rule:** every statement in this file is supported by an official primary source (URL + section + date accessed). Statements that cannot be verified are marked `[UNVERIFIED]` and are not used for annotation.

**Language convention:**
- Working language: English.
- Quotations from legal texts, official pages and model responses are kept **verbatim in the original language (FR/NL)**, followed by an English translation in square brackets when needed: `"dans les 6 mois…" [within 6 months…]`.
- Institutions are named in their official form, with both language versions where the body is bilingual, e.g. *Common Community Commission (COCOM/GGC)*. Do not translate proper names of bodies or programmes.

**Source classification (all keys).** Every source is recorded with: publisher; type (legal act / official authority page / official information portal / unofficial reproduction of a legal text / secondary); version or date; and which claim it supports. A domain name alone is not a source. Unofficial reproductions (e.g. etaamb.openjustice.be) may be used to read a legal text but are classified as such.

**When official sources disagree.** If two official sources describe the same rule differently (e.g. the legal text and an authority's guidance for citizens), the key records both, with their status. A model answer consistent with *either* official formulation is not an error; stating only one of them may be recorded as a `minor` weakness, not a material error. Only answers that contradict all official formulations are errors. Such discrepancies are reported as findings in their own right.

> **Anchoring caution.** Section Q1.5 lists what *models claimed* in the pre-existing corpus (D0). It is a checklist of points to verify, not the reference. The key is built from primary sources; anything a primary source states that no D0 response mentions still belongs in the key.

---

## 0. User profiles

| Question | Profile | Status |
|---|---|---|
| Q1. Mandatory integration programme | 40-year-old non-EU national; registering for the first time in a municipality of the Brussels-Capital Region; residence permit valid for more than three months; legally resident in Belgium for less than three years | **Unchanged from the ICML study** |
| Q2. Job-seeker registration | Lives in a Brussels municipality; valid residence and work authorisation; four years of continuous full-time work in Belgium; salaried contract in Brussels just ended — **reason for termination and benefit history: see Q2.0 (decision pending)** | Prompt approved 17:35; profile details pending |
| Q3. Recognition of a foreign diploma | Lives in the Brussels-Capital Region; Master's degree obtained outside the EU/EEA; wants to work in Brussels. **Q3 is a navigational question:** no specific profession is named, so the key specifies what a correct answer must distinguish, not a single procedure | Prompt approved |

---

## 1. Authority map (shared by Q1–Q3)

One row per function. Distinguish the **legally responsible authority** from the **operator or service provider**.

| Function | Responsible authority (level: federal / region / community / COCOM / municipality) | Operator / service provider (if different) | Legal basis | Source (URL, section) | Accessed |
|---|---|---|---|---|---|
| Q1: establishing the obligation and issuing proof of it | | | | | |
| Q1: regulation and coordination of the programme | | | | | |
| Q1: delivery — Dutch-language track | | | | | |
| Q1: delivery — French-language track | | | | | |
| Q1: enforcement and sanctions | | | | | |
| Q2: job-seeker registration | | | | | |
| Q2: ____ | | | | | |
| Q3: recognition — French Community | | | | | |
| Q3: recognition — Flemish Community | | | | | |
| Q3: ____ | | | | | |

---

## Q1. Mandatory integration programme in Brussels

### Q1.1 Checklist A (aligned with the five sub-questions of the prompt)

| # | Prompt sub-question | Correct content for this profile | Source | Not counted as an error |
|---|---|---|---|---|
| A1 | Is the programme mandatory | | | |
| A2 | Relevant exemptions **and suspensions (distinct mechanisms)** | Correct answer is conditional: mandatory *unless* an exemption applies | | An incomplete list of exemptions when none applies to the profile; a conditional rather than unconditional "yes" |
| A3 | Whom to contact (authority and/or office) | | | |
| A4 | Registration deadline, **including when the period starts** | Record the legal text (ordinance art. 5 §1) **and** the official guidance for citizens separately; see "When official sources disagree" | | Any formulation consistent with one official source |
| A5 | Completion deadline | | | |
| A6 | Choice of French- or Dutch-language track | | | |
| A7 | Current official sources | Which sources are sufficient | | |

### Q1.2 Institutional facts (used by evaluators B and C)

| # | Fact | Source | Common incorrect variants (see Q1.5) |
|---|---|---|---|
| I1 | Legal basis and dates of entry into force | | |
| I2 | Which body regulates and coordinates the programme, and since when | | |
| I3 | Role of the municipality | | |
| I4 | Which offices deliver the programme in each language | | |
| I5 | Distinction between the Brussels reception office and the Flemish agency | | |
| I6 | Sanctions for non-compliance | | |

### Q1.3 Acceptable sources

| Type of claim | Primary source | Acceptable secondary sources | Not acceptable (other jurisdiction, superseded) |
|---|---|---|---|
| Obligation, conditions, deadlines | | | |
| Offices and contacts | | | |
| Sanctions | | | |

### Q1.4 Material omissions (necessity criterion)

An omission is material only if, without the omitted information, a user with this profile **cannot correctly take the next step** or **would turn to the wrong body**.

| # | If omitted… | …the user | Material? |
|---|---|---|---|
| M1 | That the municipality establishes the obligation / issues proof of it first | | yes / no |
| M2 | When the registration period starts | | yes / no |
| M3 | That the choice of language track is free | | yes / no |
| M4 | ____ | | yes / no |

### Q1.5 Claims made in D0 responses, to be verified

Extracted from the OCR text of the 19 D0 responses. **Not the reference.** Mark each row confirmed / refuted / qualified, with a source.

| # | What models claimed | Where responses diverged | Verification result |
|---|---|---|---|
| V1 | Legal basis: COCOM ordinance of 20 July 2023; earlier ordinance of 11 May 2017 and implementing order of 19 July 2018; implementing order of 18 January 2024 | One response: "ordinance of 20 July 2023 (in force since 1 June 2022)" — internally inconsistent | |
| V2 | Obligation in force since 1 June 2022 | — | |
| V3 | Conditions: aged 18–65; first registration in the foreigners' register of a Brussels municipality; permit > 3 months; legal residence < 3 years | Some responses omit the age limits | |
| V4 | Coordination transferred to Vivalis on 1 January 2024 | Phrased variously: "instead of COCOF", "formerly COCOM", "on the French-speaking side" | |
| V5 | The municipality establishes the obligation and issues an *attestation d'obligation* / *attest van verplichting* and a brochure | — | |
| V6 | Offices: BON (Dutch track); BAPA BXL, BAPA Convivial, BAPA VIA (French track) | One response names the Flemish *Agentschap Integratie en Inburgering* for the Dutch track | |
| V7 | Registration with an office within 6 months | **Start of the period differs:** first registration in the foreigners' register / receipt of residence card and proof of obligation / notification by the municipality | |
| V8 | Completion within 18 months of registering with an office | — | |
| V9 | Administrative fine of €100–2,500 for non-compliance | — | |
| V10 | At BON, 80% attendance of each component suffices | Claimed by one response | |
| V11 | Since 1 January 2024, a right to follow the programme voluntarily for those not obliged | — | |
| V12 | Exemptions: EU/EEA/Swiss nationals and family members; temporary residence; existing integration certificate; long-term illness or disability; certain diplomas | Lists differ widely in completeness | |
| V13 | Sources: bewelcome.brussels, newcomersin.brussels, vivalis.brussels, ccc-ggc.brussels, etaamb / openjustice.be, municipal websites | Which are official, and for which claims | |

---

## Q2. Job-seeker registration

### Q2.0 Prompt and profile

Prompt: `prompts/prompts_D1.json` (approved 13 Nov 17:35). Pending profile decisions (reviewer K7–K8): reason for termination, notice period, previous unemployment benefits. Keep separate in the key: (a) registration as a jobseeker, (b) entitlement to benefits, (c) duration of benefits under the rules in force since 1 March 2026 (check the latest ONEM update, incl. any court decision), (d) payment.

### Q2.1 Checklist A

| # | Prompt sub-question | Correct content for this profile | Source | Not counted as an error |
|---|---|---|---|---|
| A1 | Where and how to register | | | |
| A2 | Which body is responsible for what (registration / benefit entitlement / payment / guidance) | | | |
| A3 | Deadlines or conditions | | | |
| A4 | Service language | | | |
| A5 | Current official sources | | | |

### Q2.2–Q2.4 Institutional facts, acceptable sources, material omissions

Tables as in Q1.2–Q1.4.

---

## Q3. Recognition of a foreign diploma in Brussels

### Q3.0 Prompt and key type

Navigational question. A correct answer must distinguish: (a) academic equivalence vs recognition of the level of a degree vs professional authorisation for a regulated profession; (b) Community competence (French Community / Flemish Community), not federal or regional; (c) that the choice between the two Communities is not fixed by place of residence; (d) public vs private sector requirements. The key must **not** require a single "Brussels authority". Use higher-education procedures only (not secondary-education equivalence pages); do not transfer fees or processing times between the two Communities.

### Q3.1 Checklist A

| # | Prompt sub-question | Correct content for this profile | Source | Not counted as an error |
|---|---|---|---|---|
| A1 | Whether recognition is needed for the user's purpose | | | |
| A2 | Competent authority (and what determines it: language, purpose, type of diploma) | | | |
| A3 | Procedure and documents | | | |
| A4 | Processing time and cost | | | |
| A5 | Current official sources | | | |

### Q3.2–Q3.4 Institutional facts, acceptable sources, material omissions

Tables as in Q1.2–Q1.4.

---

## Perturbation card (D2, completed on Saturday)

| Field | Value |
|---|---|
| Object ID / base ID | |
| Original correct fragment (verbatim, original language) | |
| Change introduced (verbatim, original language) | |
| Official source for the correct version | |
| Why the change is material for this question | |
| Expected type (T1–T5) and severity | |
| Expected detection (B and C / mainly C / neither) | |
| Approved by, timestamp | |

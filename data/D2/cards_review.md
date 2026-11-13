# D2 perturbation cards — for author approval (v2)

Bases are D1 answers **outside** the blind gold sample, so they do not appear in `D1_gold_booklet.md`; every `Before` fragment is checked by `src/build_d2.py` to occur exactly once in `data/D1/responses.jsonl`. T4 edits are deletions only. All T3 cards: expected severity minor.


## Base D1-Q1-EN-claude-r2

### T1 — registration deadline 6 → 3 months

- Reference: Q1.A4 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «register at a welcome office within six months following notification»
  After: «register at a welcome office within three months following notification»

### T2 — municipality's role (establishing the obligation, issuing the attestation) attributed to the delivery offices

- Reference: Q1.A3; Q1.I3; Q1.M1 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «Your municipality (commune) will typically first notify you of the obligation when you register.»
  After: «The BAPA or BON office will first examine whether you fall under the obligation and issue your attestation of obligation.»

### T3 — an official Brussels source replaced by a Flemish source that describes a different (Flemish) regime

- Reference: Q1.3; Q1.I5 · Expected detectors: **B (attribution) and C** · Expected severity: **minor**

- Before: «City of Brussels official portal: bruxelles.be — "Parcours d'accueil obligatoire à Bruxelles"»
  After: «Flemish government portal: vlaanderen.be — "Inburgering: verplicht inburgeringstraject" (Flemish Integration Decree)»

### T4 — municipality step and the starting event of the 6-month period removed; every remaining sentence is true

- Reference: Q1.M1; Q1.M2 · Expected detectors: **mainly C** · Expected severity: **material**

- Before: «Your municipality (commune) will typically first notify you of the obligation when you register.»
  After: «(deleted)»

- Before: «register at a welcome office within six months following notification of their obligation by their municipality.»
  After: «register at a welcome office within six months.»

### T5 — meaning-preserving rewording

- Reference: - · Expected detectors: **none** · Expected severity: **none**

- Before: «Yes, you have free choice of language track.»
  After: «Yes, the choice of language track is yours.»


## Base D1-Q1-NL-gpt-r1

### T1 — completion deadline 18 → 12 months

- Reference: Q1.A5 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «Je moet het traject **uiterlijk 18 maanden na je inschrijving/aanmelding bij BON of BAPA** afronden.»
  After: «Je moet het traject **uiterlijk 12 maanden na je inschrijving/aanmelding bij BON of BAPA** afronden.»

- Before: «het traject normaal binnen **18 maanden** afronden»
  After: «het traject normaal binnen **12 maanden** afronden»

### T2 — municipality replaced by the Flemish integration agency as the body establishing the obligation

- Reference: Q1.I3; Q1.I5; Q1.M1 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «De **gemeente** waar je je inschrijft onderzoekt eerst of je onder de verplichting valt»
  After: «Het **Agentschap Integratie en Inburgering** onderzoekt eerst of je onder de verplichting valt»

### T3 — current legal source replaced by the superseded pre-2024 version

- Reference: Q1.I1; Q1.3 · Expected detectors: **B (attribution) and C** · Expected severity: **minor**

- Before: «**Ordonnantie van 20 juli 2023 betreffende het inburgerings- en begeleidingstraject voor nieuwkomers en buitenlandse personen**, Belgisch Staatsblad / eJustice — wettelijke definitie, verplichting en vrijstellingen.»
  After: «**Ordonnantie van 11 mei 2017 betreffende het inburgeringstraject voor nieuwkomers** (versie van vóór 2024), Belgisch Staatsblad — wettelijke definitie, verplichting en vrijstellingen.»

### T4 — the free choice of language track is no longer stated; the tracks are only associated with BON (NL) and BAPA (FR)

- Reference: Q1.A6; Q1.M3 · Expected detectors: **mainly C** · Expected severity: **material**

- Before: «De gemeente informeert je dat er verschillende inrichters zijn en dat je vrij kan kiezen bij welke inrichter je het traject volgt.»
  After: «(deleted)»

- Before: «Ja. In Brussel kan je kiezen tussen:»
  After: «In Brussel bestaan:»

- Before: «; de Brusselse regeling laat echter taalkeuze binnen het Brusselse traject toe»
  After: «(deleted)»

### T5 — meaning-preserving rewording

- Reference: - · Expected detectors: **none** · Expected severity: **none**

- Before: «Er zijn twee kerntermijnen:»
  After: «Er gelden twee belangrijke termijnen:»


## Base D1-Q2-FR-gpt-r1

### T1 — Actiris registration deadline 8 → 30 calendar days (all mentions)

- Reference: Q2.A3; Q2.M1 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «dans les 8 jours civils qui suivent la fin effective»
  After: «dans les 30 jours civils qui suivent la fin effective»

- Before: «l’inscription est obligatoire dans les 8 jours suivant la fin du contrat»
  After: «l’inscription est obligatoire dans les 30 jours suivant la fin du contrat»

- Before: «2. **Dans les 8 jours civils**»
  After: «2. **Dans les 30 jours civils**»

- Before: «**Actiris dans les 8 jours civils suivant la fin du contrat**»
  After: «**Actiris dans les 30 jours civils suivant la fin du contrat**»

### T2 — exemption for training attributed to the federal ONEM/RVA instead of Actiris (regional competence since 2017)

- Reference: Q2 authority map (dispense); Q2.A4 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «| Dispense pour suivre une formation tout en gardant les allocations | **Actiris**, avec intervention pratique»
  After: «| Dispense pour suivre une formation tout en gardant les allocations | **ONEM/RVA**, avec intervention pratique»

- Before: «vous devez demander explicitement la dispense à Actiris avant de commencer»
  After: «vous devez demander explicitement la dispense à l’ONEM avant de commencer»

### T3 — federal source for the eligibility rule replaced by the Walloon employment service

- Reference: Q2.3 · Expected detectors: **B (attribution) and C** · Expected severity: **minor**

- Before: «Le SPF Emploi et l’ONEM confirment cette règle. ([emploi.belgique.be](https://emploi.belgique.be/fr/themes/chomage-et-retour-au-travail/chomage-complet?utm_source=openai))»
  After: «Le Forem confirme cette règle. ([leforem.be](https://www.leforem.be/particuliers/allocations-de-chomage.html))»

### T4 — the need for a recognised training or a prior exemption request is removed (deletions only)

- Reference: Q2.M3; Q2.A4 · Expected detectors: **mainly C** · Expected severity: **material**

- Before: «Attention : si la formation n’est pas une formation professionnelle agréée ou automatiquement couverte — par exemple études supérieures, formation privée, stage à l’étranger, etc. — vous devez demander explicitement la dispense à Actiris avant de commencer, au moyen du formulaire approprié. ([hvw-capac.fgov.be](https://hvw-capac.fgov.be/fr/aide/etudes/region-de-bruxelles-capitale))»
  After: «(deleted)»

- Before: «- vérifiez avec Actiris/CAPAC/syndicat que la dispense est bien automatique ou, sinon, demandez-la avant le début.»
  After: «(deleted)»

### T5 — meaning-preserving rewording

- Reference: - · Expected detectors: **none** · Expected severity: **none**

- Before: «inscrivez-vous dès le lendemain du dernier jour de travail»
  After: «inscrivez-vous dès le lendemain de votre dernier jour de travail»


## Base D1-Q2-NL-claude-r1

### T1 — benefit duration 12+12=24 → 24+12=36 months

- Reference: Q2.A3; Q2.I1 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «beperkt tot maximum 24 maanden. Dat recht omvat een basisperiode van 12 maanden»
  After: «beperkt tot maximum 36 maanden. Dat recht omvat een basisperiode van 24 maanden»

- Before: «hoe dichter je bij de 24 maanden komt»
  After: «hoe dichter je bij de 36 maanden komt»

- Before: «(maximaal 24 maanden)»
  After: «(maximaal 36 maanden)»

### T2 — payment of benefits attributed to Actiris instead of a payment body (CAPAC/HVW or union)

- Reference: Q2.A2; Q2.I3; Q2.M2 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «| **Uitbetaling** van de uitkering | Een **uitbetalingsinstelling** naar keuze: ABVV, ACV, SYNOVA (vakbonden) of de **HVW/CAPAC** (openbare instelling) |»
  After: «| **Uitbetaling** van de uitkering | **Actiris** (gewestelijke dienst) |»

- Before: «Actiris betaalt zelf geen werkloosheidsuitkeringen uit.»
  After: «Actiris betaalt de werkloosheidsuitkeringen uit.»

### T3 — the Brussels exemption source replaced by a Flemish one written for residents of Flanders

- Reference: Q2.3; S44 · Expected detectors: **B (attribution) and C** · Expected severity: **minor**

- Before: «- Actiris – "Vrijstelling van beschikbaarheid" (actiris.brussels)»
  After: «- VDAB – "Vrijstelling van beschikbaarheid voor werkzoekenden in Vlaanderen" (vdab.be)»

### T4 — the 8-day registration deadline and its consequence removed

- Reference: Q2.M1; Q2.A1 · Expected detectors: **mainly C** · Expected severity: **material**

- Before: «inschrijven als werkzoekende op de dag van de aanvraag of binnen de 8 daaropvolgende kalenderdagen. Let op: indien deze termijn niet in acht wordt genomen, kun je slechts uitkeringen ontvangen vanaf de dag van de inschrijving.»
  After: «inschrijven als werkzoekende.»

- Before: «Schrijf je **nu** (binnen 8 kalenderdagen na het einde van je opzegtermijn) in»
  After: «Schrijf je **nu** in»

### T5 — meaning-preserving rewording

- Reference: - · Expected detectors: **none** · Expected severity: **none**

- Before: «Vraag meteen een uitkering aan;»
  After: «Vraag onmiddellijk een uitkering aan;»


## Base D1-Q3-EN-gpt-r1

### T1 — bilingual-employer rule reversed (free choice → NARIC-Vlaanderen only)

- Reference: Q3.I2; Q3.A2 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «NARIC-Vlaanderen says you may apply either to NARIC-Vlaanderen or to the French Community NARIC centre, and you should ask the future employer which they prefer.»
  After: «NARIC-Vlaanderen says you must apply to NARIC-Vlaanderen; the French Community service cannot be used for bilingual employers.»

### T2 — the FWB higher-education recognition service replaced by Actiris (a Regional body, not competent)

- Reference: Q3.I1; Q3.A2; Q3.M4 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «For higher-education diplomas, the competent service is the **Service de la reconnaissance académique et professionnelle des diplômes étrangers d’enseignement supérieur** of the Fédération Wallonie-Bruxelles.»
  After: «For higher-education diplomas, the competent service is **Actiris**, the Brussels regional employment service, which issues equivalence decisions for Brussels residents.»

### T3 — the Brussels Region page replaced by the ENIC-NARIC page for France as support for a statement about Brussels

- Reference: Q3.3 · Expected detectors: **B (attribution) and C** · Expected severity: **minor**

- Before: «sources for diploma equivalence. ([be.brussels](https://be.brussels/en/education-teaching/equivalence-diplomas))   ⏎  ⏎ **Practical tip:**»
  After: «sources for diploma equivalence. ([enic-naric.net](https://www.enic-naric.net/page-france))   ⏎  ⏎ **Practical tip:**»

### T4 — the rule linking the authority to the language/community of the job and the instruction to identify the job type are removed (deletions only)

- Reference: Q3.M1; Q3.A2 · Expected detectors: **mainly C** · Expected severity: **material**

- Before: «- If the employer or vacancy is linked to the **French-speaking sector**, use the **Fédération Wallonie-Bruxelles** route. ⏎ - If the employer or vacancy is linked to the **Dutch-speaking/Flemish sector**, use **NARIC-Vlaanderen**.»
  After: «(deleted)»

- Before: «First identify whether the Brussels job is **non-regulated private-sector**, **public-sector/subsidised**, or a **regulated profession**; then ask»
  After: «Ask»

### T5 — meaning-preserving rewording

- Reference: - · Expected detectors: **none** · Expected severity: **none**

- Before: «That can save time and money.»
  After: «This can save you time and money.»


## Base D1-Q3-FR-claude-r1

### T1 — regulated professions: specific equivalence replaced by level equivalence

- Reference: Q3.A3; Q3.M3 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «L'équivalence est **obligatoire et doit être spécifique** (pas seulement de niveau) :»
  After: «L'équivalence est **obligatoire** ; une équivalence de niveau suffit :»

- Before: «Une équivalence de niveau d'études ne permet pas d'exercer une profession règlementée en Belgique francophone. Il faut donc une équivalence à un grade académique spécifique.»
  After: «Une équivalence de niveau d'études suffit pour exercer une profession règlementée en Belgique francophone.»

### T2 — Community competence presented as a Regional competence exercised by Actiris

- Reference: Q3.I1; Q3.A2 · Expected detectors: **B and C** · Expected severity: **material**

- Before: «La reconnaissance des diplômes est une compétence communautaire (et non régionale), ce qui crée une particularité pour Bruxelles : la reconnaissance des diplômes étrangers est une matière communautaire.»
  After: «La reconnaissance des diplômes est une compétence régionale : à Bruxelles, c'est la Région de Bruxelles-Capitale, via Actiris, qui délivre les équivalences.»

### T3 — official Brussels portal replaced by the Walloon Region portal

- Reference: Q3.3 · Expected detectors: **B (attribution) and C** · Expected severity: **minor**

- Before: «- **be.brussels** (portail officiel de la Région de Bruxelles-Capitale) :»
  After: «- **wallonie.be** (portail officiel de la Région wallonne) :»

- Before: «https://be.brussels/fr/education-enseignement/equivalence-des-diplomes»
  After: «https://www.wallonie.be/fr/demarches/obtenir-lequivalence-dun-diplome-etranger»

### T4 — the public-sector requirement is removed (deletions only)

- Reference: Q3.M2; Q3.A1 · Expected detectors: **mainly C** · Expected severity: **material**

- Before: «En revanche, l'équivalence ou la reconnaissance de votre diplôme est obligatoire pour exercer une profession réglementée OU non réglementée dans le secteur public ou les institutions subsidiées par les pouvoirs publics.»
  After: «(deleted)»

- Before: «**b) Emploi (non réglementé) dans le secteur public** ⏎ Ici l'équivalence devient **obligatoire**, même si la profession elle-même n'est pas réglementée : quelle que soit l'état d'origine du diplôme, la personne qui souhaite exercer une profession non réglementée dans le secteur public ou dans une institution subventionnée par les pouvoirs publics doit demander l'équivalence de son diplôme étrange …»
  After: «(deleted)»

- Before: «travailler dans la fonction publique ou exercer une profession réglementée»
  After: «exercer une profession réglementée»

### T5 — meaning-preserving rewording

- Reference: - · Expected detectors: **none** · Expected severity: **none**

- Before: «Non, cela dépend du type d'emploi.»
  After: «Non, tout dépend du type d'emploi.»

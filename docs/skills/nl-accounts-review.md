---
description: 'Run an analytical review of one or more Dutch companies'' annual accounts (jaarrekening) filed at the Kamer van Koophandel (KvK). Input is a list of KvK numbers; output is a structured multi-file audit deliverable: main report, findings register, ratio matrix with RAG flags, and (for groups) an indicative consolidation + deelneming impairment scan.'
title: nl-accounts-review
---

# nl-accounts-review

Run an analytical review of one or more Dutch companies' annual accounts (jaarrekening) filed at the Kamer van Koophandel (KvK). Input is a list of KvK numbers; output is a structured multi-file audit deliverable: main report, findings register, ratio matrix with RAG flags, and (for groups) an indicative consolidation + deelneming impairment scan.

| | |
|---|---|
| **Area** | Finance |
| **Category** | finance |
| **Level** | advanced |
| **Input** | data |
| **Output** | spreadsheet |
| **Setup** | [install] |
| **Roles** | [Finance Manager] |

Reviews Dutch annual accounts (jaarrekening) filed at KvK (Kamer van Koophandel).

## How you ask

- “Analytical review”
- “Audit-style report”
- “Counterparty financial check”

## Inputs

- kvk_number — 8-digit KvK number, with or without dashes (e.g. {kvk-number})
- years — Number of fiscal years to review (current + N-1 priors)
- sbi_code — SBI code (Dutch CBS equivalent of NACE) for sector benchmarking; defaults to generic SME bands
- client_id — If provided, deliverables route to the client folder (`client.root`) instead of scratch (`output.scratch`)
- parent_kvk_number — Parent kvk number used to review parent + N subsidiaries with indicative consolidation, deelneming impairment scan, and cross-guarantee analysis
- subsidiary_kvk_numbers — List of KvK numbers; if empty, attempt to extract from parent's toelichting participations disclosure
- years — Years used to review parent + N subsidiaries with indicative consolidation, deelneming impairment scan, and cross-guarantee analysis
- client_id — Client id used to review parent + N subsidiaries with indicative consolidation, deelneming impairment scan, and cross-guarantee analysis
- parent_kvk_number — Parent kvk number used to standalone scan of parent's financiële vaste activa (deelnemingen) vs subsidiary eigen vermogen
- subsidiary_kvk_numbers — Subsidiary kvk numbers used to standalone scan of parent's financiële vaste activa (deelnemingen) vs subsidiary eigen vermogen

## Outputs

- audit_report (markdown)
- findings_register (markdown)
- group_report_bundle (markdown)
- impairment_scan (markdown)
- prefer a permanent directory)
- ratios_and_anomalies (markdown)


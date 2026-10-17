---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: be-accounts-review — ThirdBrain BOB skill
  description: Run an analytical review of one or more Belgian companies' deposited annual accounts. Input is a list of enterprise numbers (KBO/BCE); output is a structured mu
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: be-accounts-review
catLabel: finance
area: finance
desc: Reviews Belgian statutory accounts deposited at NBB and produces an analytical report.
summary: 'Run an analytical review of one or more Belgian companies'' deposited annual accounts. Input is a list of enterprise numbers (KBO/BCE); output is a structured multi-file audit deliverable: main report, findings register, ratio matrix with RAG flags, and (for groups) an indicative consolidation + deelneming impairment scan.'
difficulty: advanced
inputType: data
outputType: spreadsheet
requires: '[install]'
roles: '[Finance Manager]'
inputs:
- enterprise_number — 10-digit KBO/BCE number, with or without dots (e.g. {enterprise-number} or {enterprise-number})
- years — Number of fiscal years to review (current + N-1 priors)
- nace_code — NACE code for sector benchmarking; defaults to generic SME bands
- client_id — If provided, deliverables route to the client folder (`client.root`) instead of scratch (`output.scratch`)
- parent_enterprise_number — Parent enterprise number used to review parent + N subsidiaries with indicative consolidation, deelneming impairment scan, and cross-guarantee analysis
- subsidiary_enterprise_numbers — List of KBO numbers; if empty, attempt to extract from parent's VOL-kap 6.5.1
- years — Years used to review parent + N subsidiaries with indicative consolidation, deelneming impairment scan, and cross-guarantee analysis
- client_id — Client id used to review parent + N subsidiaries with indicative consolidation, deelneming impairment scan, and cross-guarantee analysis
- parent_enterprise_number — Parent enterprise number used to standalone scan of parent's financial fixed assets vs subsidiary EV
- subsidiary_enterprise_numbers — Subsidiary enterprise numbers used to standalone scan of parent's financial fixed assets vs subsidiary EV
outputs:
- audit_report (markdown)
- findings_register (markdown)
- group_report_bundle (markdown)
- impairment_scan (markdown)
- prefer a permanent directory)
- ratios_and_anomalies (markdown)
prompts:
- KBO/BCE
- Analytical review
- Audit-style report
---

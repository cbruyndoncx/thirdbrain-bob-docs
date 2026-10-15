---
description: 'Target Audience: Claims consultants, project directors, quantity surveyors, and contract administrators preparing FIDIC EOT claims in UAE/GCC construction projects.'
title: eot-claims-preparer
---

# eot-claims-preparer

Target Audience: Claims consultants, project directors, quantity surveyors, and contract administrators preparing FIDIC EOT claims in UAE/GCC construction projects.

| | |
|---|---|
| **Area** | Operations |
| **Category** | engineering |
| **Level** | expert |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [mcp, api-key] |
| **Roles** | [Operations Manager] |

Structure Extension of Time claims with FIDIC-compliant notices, delay narratives, evidence marshalling, and Engineer determination templates.

## How you ask

- “Scan the project correspondence for anything that needs a notice”
- “Draft a 28-day notice for a delay caused by late Employer drawings”
- “Prepare a detailed EOT claim for the site access delay on Project X”
- “Check if our existing notices comply with FIDIC 2017 requirements”
- “How many days can we claim for the variation-related delay?”

## Inputs

- records — Correspondence directory to scan (letters, emails, minutes, site records)
- edition — FIDIC edition — 1999 or 2017 (default 2017)
- event-description — Description of the delay event and when awareness occurred
- contract-basis — Relevant sub-clause entitlement basis
- event-description — Delay event details, dates, and impact
- schedule-data — Baseline schedule, critical path, and current status
- existing-notices — Existing notices/claims to audit for compliance

## Outputs

- claim-package (markdown)
- compliance-report (markdown)
- notice-letter (markdown)
- notice-register (markdown)
- {project-folder}/eot_claim_{date}.md
- {project-folder}/eot_compliance_check.md
- {project-folder}/eot_notice_{date}.md
- {project-folder}/notice_register.md

## Seen in these workflows

- [Eot Claims Preparer](../workflows/eot-claims-preparer.md)


---
description: 'Target Audience: PMC firms, Engineers, project directors, and contract administrators who must issue formal responses to contractor claims under FIDIC construction contracts.'
title: contractor-claims-response
---

# contractor-claims-response

Target Audience: PMC firms, Engineers, project directors, and contract administrators who must issue formal responses to contractor claims under FIDIC construction contracts.

- **Area:** Operations
- **Category:** engineering
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Analyze and respond to contractor claims (Force Majeure, EOT, price escalation, Special Risk, variation, payment) under FIDIC construction contracts.

## How you ask

- “Contractor letter”
- “Respond to claim”
- “Contractor notice”

## Inputs

- claim-letter — Full text or summary of the contractor's claim letter
- contract-context — NotebookLM alias, pasted clauses, or local contract note for the current matter
- matter-context — Company folder, lead slug, client_id, or project folder used to route outputs
- claim-letters — Full text or summaries of all contractor claim letters
- claim-letter — Contractor's letter to audit for notice compliance
- contract-context — Particular Conditions notice deadline source for the current matter

## Outputs

- Running claim register, appended with one `claim_record` per response in the same `context-folder` as the response package — company, lead, client-account or client-project, per Step 0.
- audit-report (markdown)
- response-package (markdown)
- {company.legal}/claim_register.md
- {context-folder}/notice_compliance_audit_{ref}_{date}.md
- {context-folder}/response_combined_{topic}_{date}.md
- {context-folder}/response_{ref}_{date}.md


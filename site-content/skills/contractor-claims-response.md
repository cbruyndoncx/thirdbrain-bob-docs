---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: contractor-claims-response — ThirdBrain BOB skill
  description: 'Target Audience: PMC firms, Engineers, project directors, and contract administrators who must issue formal responses to contractor claims under FIDIC construct'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: contractor-claims-response
catLabel: engineering
area: operations
desc: Analyze and respond to contractor claims (Force Majeure, EOT, price escalation, Special Risk, variation, payment) under FIDIC construction contracts.
summary: 'Target Audience: PMC firms, Engineers, project directors, and contract administrators who must issue formal responses to contractor claims under FIDIC construction contracts.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- claim-letter — Full text or summary of the contractor's claim letter
- contract-context — NotebookLM alias, pasted clauses, or local contract note for the current matter
- matter-context — Company folder, lead slug, client_id, or project folder used to route outputs
- claim-letters — Full text or summaries of all contractor claim letters
- claim-letter — Contractor's letter to audit for notice compliance
- contract-context — Particular Conditions notice deadline source for the current matter
outputs:
- Running claim register, appended with one `claim_record` per response in the same `context-folder` as the response package — company, lead, client-account or client-project, per Step 0.
- audit-report (markdown)
- response-package (markdown)
- '{company.legal}/claim_register.md'
- '{context-folder}/notice_compliance_audit_{ref}_{date}.md'
- '{context-folder}/response_combined_{topic}_{date}.md'
- '{context-folder}/response_{ref}_{date}.md'
prompts:
- Contractor letter
- Respond to claim
- Contractor notice
---

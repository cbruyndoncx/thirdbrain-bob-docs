---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: escalation-routing — ThirdBrain BOB skill
  description: Route issues, complaints, and problems to the appropriate level when the current handler cannot resolve them.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: escalation-routing
catLabel: qms
area: operations
desc: Routes already-triaged issues up the chain when first-line handling is insufficient.
summary: Route issues, complaints, and problems to the appropriate level when the current handler cannot resolve them.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- issue — The problem to triage, in the reporter's own words
- severity — assessed from impact if omitted (p1 | p2 | p3 | p4)
- client_id — Client affected, when client-scoped
- profile — Company or client profile — sector and operating context.
- issue_ref — Issue being escalated
- audience — sets tone and detail level (internal | client | executive)
- org_context — Team structure, roles, and who owns which decision
- sla_targets — Response and resolution targets per severity
outputs:
- escalation-handoff (markdown)
- escalation-paths (markdown)
- triage-decision (markdown)
- '{company.qms.root}/escalation-routing-{YYYY-MM-DD}.md'
prompts:
- Assess the severity level of this customer complaint
- Route this technical issue to the right team
- Document the escalation decision for this support case
- Apply routing rules to triage this incoming issue
---

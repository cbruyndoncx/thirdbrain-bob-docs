---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: owner-priority-system — ThirdBrain BOB skill
  description: The runtime engine of the Owner Operating System. Reads company signals, computes health-domain scores, runs the data-quality gate, identifies the binding const
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: owner-priority-system
catLabel: business
area: strategy
desc: Turns company state and operating signals into a concise owner priority brief — diagnoses current business state, identifies binding constraint, ranks evidence, sets top…
summary: The runtime engine of the Owner Operating System. Reads company signals, computes health-domain scores, runs the data-quality gate, identifies the binding constraint, and writes the recommendation back to `CURRENT-STATE.md`.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder]'
inputs:
- current-state — CURRENT-STATE.md, under the management tree (`company.management`) — prior state for delta comparison
- kpi-registry — KPI-REGISTRY.md, under the management tree (`company.management`) — thresholds and source mappings
- horizon — Planning horizon — weekly sets next-week priorities, monthly sets next-month (weekly | monthly)
- current-state — CURRENT-STATE.md, under the management tree (`company.management`)
- current-state — CURRENT-STATE.md, under the management tree (`company.management`) (must have business_state + binding_constraint set)
outputs:
- brief (markdown)
- diagnosis (markdown)
- priorities (markdown)
- route (markdown)
- '{company.management}/CURRENT-STATE.md'
- '{company.management}/briefs/{YYYY-MM-DD}_owner_brief.md'
prompts:
- What should I focus on now
- What's my biggest problem
- Where am I leaking
---

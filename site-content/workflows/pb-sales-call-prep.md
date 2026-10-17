---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Sales Call Prep — BOB Workflow
  description: Sales Call Prep
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-sales-call-prep
youtubeId: ''
published: ''
privacy: unlisted
title: Sales Call Prep
thumbnail: ''
subtitle: Rep enters the call with a clear opener, stakeholder context, call goal, likely friction points, and the next step to secure
inputs: []
outputs: []
steps:
- label: vault-preflight → verify that company, deal, and prior-note context are loaded enough to produce a useful prep brief
  actor: agent
- label: research-company → gather or refresh company intelligence relevant to the scheduled conversation
  actor: agent
- label: meeting-intelligence → use prep context from prior meetings, unresolved actions, and relationship history when available
  actor: agent
- label: consultative-selling → generate the stage-appropriate question set, framing, or proof logic for this specific call type
  actor: agent
- label: Build the prep brief with opener insight, stakeholder context, likely friction, and desired call outcome
  actor: agent
- label: Review and trim the brief so the rep can realistically use it live without overload
  actor: human
- label: After the call, hand off to [[meeting-intelligence]] for debrief and update any resulting next action in [[crm-pipeline]]
  actor: agent
trigger: '"A discovery, demo, proposal-review, or negotiation call is scheduled and the rep needs a fast, high-signal briefing"'
timeSavings: 'Typical run: 20-45 minutes depending on deal complexity and available context'
compounding: Each run refines templates and context — 6 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'Call starts in ten minutes.

  You''re about to improvise the opener.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---



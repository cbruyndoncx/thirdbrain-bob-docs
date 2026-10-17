---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Mutual Action Plan — BOB Workflow
  description: Mutual Action Plan
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-mutual-action-plan
youtubeId: ''
published: ''
privacy: unlisted
title: Mutual Action Plan
thumbnail: ''
subtitle: Internal close plan built, buyer-facing mutual action plan prepared when appropriate, and deal path to signature made explicit
inputs: []
outputs:
- label: Internal Close Plan.md
  icon: 🗺️
- label: Mutual Action Plan.md
  icon: 🗺️
- label: Updated deal note in [[crm-pipeline]]
  icon: 📅
steps:
- label: vault-preflight → confirm the deal record, stage, and latest notes exist before planning against stale information
  actor: agent
- label: crm-pipeline → read current stage, next action, due dates, and pipeline activity to establish the live deal state
  actor: agent
- label: MEDDPICC Qualification → extract decision process, paper process, economic buyer access, and known procurement dependencies
  actor: agent
- label: meeting-intelligence → extract latest commitments, open questions, and whether a concrete next step was actually secured
  actor: agent
- label: Review the plan and separate what stays internal from what can be shared with the buyer
  actor: human
- label: negotiation → prepare responses for milestones that carry commercial, legal, or procurement friction
  actor: agent
- label: crm-pipeline → sync the single most important next action and due date back to the deal record so weekly pipeline review stays accurate
  actor: agent
trigger: '"Active deal needs an explicit path to signature with milestones, owners, and decision checkpoints"'
timeSavings: 'Typical run: 45-90 minutes to establish; 10-20 minutes to update after each material deal event'
compounding: Each run refines templates and context — 6 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'Everyone says the deal is closing.

  Nobody can say by when, or how.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---



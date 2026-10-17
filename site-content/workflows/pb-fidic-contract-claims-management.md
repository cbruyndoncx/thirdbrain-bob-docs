---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: FIDIC Contract Claims Management — BOB Workflow
  description: FIDIC Contract Claims Management
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-fidic-contract-claims-management
youtubeId: ''
published: ''
privacy: unlisted
title: FIDIC Contract Claims Management
thumbnail: ''
subtitle: FIDIC Claims Lifecycle
inputs:
- label: contract-docs.pdf
  icon: 📜
- label: baseline-schedule.xlsx
  icon: 📊
- label: site-records
  icon: 📁
outputs:
- label: risk_register.md
  icon: ⚠️
- label: variation_register.md
  icon: 📋
- label: eot_claim.md
  icon: 📕
steps:
- project-context → establish baseline
- contract-clause-analyzer → risk register
- label: Review high-risk clauses
  actor: human
- variation-order-analyzer → assess VOs
- delay-analysis-tool → run TIA
- eot-claims-preparer → draft notice
- label: Review and submit claim
  actor: human
trigger: '"New FIDIC project awarded — set up claims readiness"'
timeSavings: Weeks of manual work → hours with agent assistance
compounding: Each claim strengthens the precedent library across projects
frequency: Per project · per delay event
hook: 'New FIDIC project.

  Claims readiness starts now, not when things go wrong.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: project-delivery
---



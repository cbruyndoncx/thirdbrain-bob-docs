---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Cash Control Routine — BOB Workflow
  description: Cash Control Routine
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-cash-control-routine
youtubeId: ''
published: ''
privacy: unlisted
title: Cash Control Routine
thumbnail: ''
subtitle: Cash Position and AR Followup
inputs:
- label: bank-balance.md
  icon: 💰
- label: invoice-ledger.xlsx
  icon: 📊
outputs:
- label: cash_position.md
  icon: 💰
- label: ar_actions.md
  icon: 📨
- label: escalation_plan.md
  icon: ⚠️
steps:
- financial-reporting → cash position
- label: Confirm severity level
  actor: human
- ar-followup → chase overdue invoices
- collections-escalation → 60+ day plan
- label: Approve escalation actions
  actor: human
- invoice-collector → reconcile payments
trigger: '"Cash is tight" or monthly review'
timeSavings: ~4 hrs manual → ~30 min automated
compounding: AR patterns emerge — repeat offenders flagged earlier each cycle
frequency: Monthly · or on cash pressure
hook: 'Cash is tight.

  And nobody has chased the invoices.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: finance
---



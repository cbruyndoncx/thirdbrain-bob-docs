---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Win Loss Review — BOB Workflow
  description: Win Loss Review
  socialImage: https://img.youtube.com/vi/uPFO6levyL8/maxresdefault.jpg
skillName: pb-win-loss-review
youtubeId: uPFO6levyL8
published: '2026-04-22'
privacy: public
title: Win Loss Review
thumbnail: https://img.youtube.com/vi/uPFO6levyL8/maxresdefault.jpg
subtitle: Capture Why, Feed Back to Sales
inputs:
- label: deal-context.md
  icon: 📝
- label: proposal.pdf
  icon: 📄
- label: meeting-notes.md
  icon: 📋
outputs:
- label: win_loss_report.md
  icon: 📊
- label: sales_enablement.md
  icon: 📝
steps:
- label: Gather deal context
  actor: human
- meeting-intelligence → analyze interactions
- label: Add relationship context
  actor: human
- content-repurposer → extract insights
- label: Decide what to operationalize
  actor: human
- Update objection playbook and positioning
trigger: '"Run win loss review" after deal closes'
timeSavings: ~2 hrs manual post-mortem → ~30 min automated
compounding: Win/loss patterns emerge — objection handling improves each cycle
frequency: Per closed deal
hook: 'You won some. You lost more.

  Nobody wrote down why.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Capture Why, Feed Back to Sales


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

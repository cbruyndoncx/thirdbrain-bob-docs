---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Monthly Business Review — BOB Workflow
  description: Monthly Business Review
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-monthly-business-review
youtubeId: ''
published: ''
privacy: unlisted
title: Monthly Business Review
thumbnail: ''
subtitle: Close Month, Set Priorities
inputs:
- label: last-month-priorities.md
  icon: 📋
- label: financial-data
  icon: 💰
outputs:
- label: monthly_review.md
  icon: 📊
- label: pipeline_health.md
  icon: 📈
- label: priorities_next_month.md
  icon: 🎯
steps:
- financial-reporting → P&L and cash
- business-reporting → month-over-month
- label: Flag anomalies
  actor: human
- crm-pipeline → pipeline health
- project-status → delivery status
- label: Identify binding constraint
  actor: human
- prioritization-craft → RICE priorities
trigger: '"Run monthly review" or first week of month'
timeSavings: ~6 hrs manual → ~60 min automated
compounding: Trend detection sharpens — each review builds on prior months
frequency: Monthly
hook: 'Another month gone.

  No review, no trend, same priorities as last month.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: finance
---



---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Weekly Business Review — BOB Workflow
  description: Weekly Business Review
  socialImage: https://img.youtube.com/vi/NhDkOvihzgc/maxresdefault.jpg
skillName: pb-weekly-business-review
youtubeId: NhDkOvihzgc
published: '2026-04-22'
privacy: public
title: Weekly Business Review
thumbnail: https://img.youtube.com/vi/NhDkOvihzgc/maxresdefault.jpg
subtitle: Maintain Operating Grip
inputs:
- label: carryover-items.md
  icon: 📋
- label: upcoming-events.md
  icon: 📅
outputs:
- label: pipeline_snapshot.md
  icon: 📊
- label: cash_position.md
  icon: 💰
- label: weekly_priorities.md
  icon: 🎯
steps:
- crm-pipeline → pipeline snapshot
- label: Flag stalled deals
  actor: human
- financial-reporting → cash position
- client-health-tracker → active client scan
- label: Set top 3 priorities
  actor: human
trigger: '"Run weekly review" or every Monday'
timeSavings: ~2 hrs manual → ~30 min automated
compounding: Stalled deal patterns emerge — earlier intervention each week
frequency: Weekly
hook: 'Monday again.

  Pipeline, cash, priorities — all somewhere in your head.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---

Maintain Operating Grip


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

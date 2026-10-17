---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Quarterly Replan — BOB Workflow
  description: Quarterly Replan
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-quarterly-replan
youtubeId: ''
published: ''
privacy: unlisted
title: Quarterly Replan
thumbnail: ''
subtitle: Strategic Reset
inputs:
- label: last-quarter-results.md
  icon: 📊
- label: strategic-constraints.md
  icon: 🎯
outputs:
- label: growth_diagnosis.md
  icon: 📈
- label: quarterly_okrs.md
  icon: 🎯
- label: quarter_timeline.md
  icon: 📅
steps:
- business-baseline → current state map
- growth-scaling-playbook → diagnose stage
- label: Confirm growth stage
  actor: human
- strategy-frameworks → strategic choices
- okr-frameworks → draft OKRs
- label: Adjust OKRs
  actor: human
- prioritization-craft → RICE initiatives
- project-schedule → quarter timeline
trigger: '"Quarterly replan" or start of quarter'
timeSavings: ~2 days strategic offsite → ~2 hrs automated
compounding: Each quarter builds on prior diagnosis — strategic drift detected faster
frequency: Quarterly
hook: 'New quarter.

  Same plan you stopped believing in weeks ago.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---



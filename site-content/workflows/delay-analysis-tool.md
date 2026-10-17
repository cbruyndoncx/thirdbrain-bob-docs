---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Delay Analysis Tool — BOB Workflow
  description: 'Target Audience: Project schedulers, claims consultants, project directors, and PMC firms performing delay analysis on FIDIC construction projects in UAE/GCC.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: delay-analysis-tool
youtubeId: ''
published: ''
privacy: unlisted
title: Delay Analysis Tool
thumbnail: ''
subtitle: Time Impact Analysis (TIA)
inputs:
- label: approved-baseline.xlsx
  icon: 📊
- label: delay-event-description.md
  icon: ⏱️
outputs:
- label: tia_report.md
  icon: 📋
- label: concurrent_delay_assessment.md
  icon: ⚖️
steps:
- Establish baseline and critical path
- Define delay event
- Construct and insert fragnet
- Recalculate CPM
- label: Verify net delay figure
  actor: human
- Compile TIA report
trigger: '"Analyze the delay impact of 3 weeks late site access on our critical path"'
timeSavings: ~1-2 days manual CPM analysis → ~20 min automated
compounding: Each TIA strengthens the project delay record — cumulative evidence for arbitration
frequency: Per delay event · monthly schedule update
hook: 'The project is late.

  Proving whose fault it is takes weeks.'
outcome: ''
benefits: []
cta: ''
difficulty: expert
primaryRoles:
- Operations Manager
pricingTier: pack-engineering-pro
category: engineering
filterGroup: engineering
area: operations
---

**Target Audience:** Project schedulers, claims consultants, project directors, and PMC firms performing delay analysis on FIDIC construction projects in UAE/GCC.

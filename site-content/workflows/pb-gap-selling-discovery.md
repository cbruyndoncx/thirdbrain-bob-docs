---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Gap Selling Discovery — BOB Workflow
  description: Gap Selling Discovery
  socialImage: https://img.youtube.com/vi/3jQ7bywBb-g/maxresdefault.jpg
skillName: pb-gap-selling-discovery
youtubeId: 3jQ7bywBb-g
published: '2026-08-01'
privacy: public
title: Gap Selling Discovery
thumbnail: https://img.youtube.com/vi/3jQ7bywBb-g/maxresdefault.jpg
subtitle: Current State and Future State mapped, gap quantified in dollars and performance metrics, urgency created, solution positioned as the bridge
inputs:
- label: Prospect company name and URL
  icon: 🏢
- label: Contact name and role
  icon: 👤
- label: Industry benchmarks (average performance, peer comparison data)
  icon: 🏭
- label: Known pain points or triggers (if any prior discovery)
  icon: 📋
- label: Your service offering and pricing range
  icon: 💰
outputs:
- label: Question Bank.md
  icon: 📋
- label: State Map.md
  icon: 🗺️
- label: Gap Analysis.md
  icon: 📊
- label: Cost-of-Inaction Model.md
  icon: 💰
- label: Diagnostic Brief.md
  icon: 📋
steps:
- label: research-company → gather company intelligence, current performance indicators, technology stack, competitive position
  actor: agent
- label: 'consultative-selling → generate Gap Selling discovery question bank: Current State mapping questions, Future State vision questions, gap quantification prompts'
  actor: agent
- label: Review question bank, prepare industry benchmarks and gap data for the call
  actor: human
- label: 'Conduct discovery call: map Current State (processes, tools, performance, costs) → define Future State (ideal outcomes, capabilities, metrics) → quantify the gap together'
  actor: human
- label: meeting-intelligence → extract Current State facts, Future State vision, gap dimensions, and urgency signals from call notes
  actor: agent
- label: 'consultative-selling → build gap analysis document: quantify financial gap, performance gap, time gap, capability gap; model cost of inaction over 3-6-12 months'
  actor: agent
- label: Review gap analysis, validate numbers, prepare urgency framing and solution positioning
  actor: human
- label: consultative-selling → generate diagnostic brief positioning your solution as the bridge from Current to Future State, with ROI calculation and proof points
  actor: agent
trigger: '"Prospect is comfortable with status quo, no urgency to change — need to surface and quantify the gap between current and future state"'
timeSavings: 'Typical run: 2-4 hours across pre-call prep, discovery call, and gap analysis documentation'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'The prospect is fine as they are.

  Until someone puts a number on the gap.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Current State and Future State mapped, gap quantified in dollars and performance metrics, urgency created, solution positioned as the bridge


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

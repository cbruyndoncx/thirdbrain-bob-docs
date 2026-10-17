---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Grow My Revenue — BOB Workflow
  description: Grow My Revenue
  socialImage: https://img.youtube.com/vi/ZqMwZoE92uQ/maxresdefault.jpg
skillName: pb-grow-my-revenue
youtubeId: ZqMwZoE92uQ
published: '2026-08-01'
privacy: public
title: Grow My Revenue
thumbnail: https://img.youtube.com/vi/ZqMwZoE92uQ/maxresdefault.jpg
subtitle: Diagnosed growth constraint with targeted 90-day action plan spanning pricing, acquisition, conversion, or product-led growth
inputs:
- label: Business name and industry
  icon: 🏢
- label: Current annual revenue and growth rate
  icon: 📋
- label: Top 3 revenue concerns (in the owner's own words)
  icon: 📋
- label: Team size and available capacity
  icon: 📋
- label: Budget for growth initiatives (if any)
  icon: 💰
- label: Current sales/marketing channels
  icon: 📋
- label: Biggest recent win and biggest recent loss
  icon: 📋
outputs:
- label: ICP Profile.md
  icon: 🎯
- label: Growth Diagnosis.md
  icon: 📋
- label: Route Deliverables.md
  icon: 📋
- label: 90-Day Plan.md
  icon: 🗺️
- label: Branded Report.pdf
  icon: 📊
steps:
- label: vault-preflight → verify client context completeness and flag blocking gaps before proceeding
  actor: agent
- label: icp-discovery → define or refine ideal customer profile for primary revenue stream
  actor: agent
- label: product-marketing-context → establish positioning, messaging, and competitive landscape
  actor: agent
- label: Review ICP and positioning — confirm accuracy before diagnosis
  actor: human
- label: growth-scaling-playbook → diagnose growth stage, identify binding constraint, and recommend 90-day focus
  actor: agent
- label: Review diagnosis — confirm binding constraint and select 1-2 routes below to maintain focus
  actor: human
- label: Integrate outputs into 90-day action plan with 3-5 priorities, owners, deadlines, and success metrics — update crm-pipeline with any new deals or stage changes
  actor: agent
- label: pdf-report → generate branded PDF of the 90-day action plan with diagnosis summary, route outputs, and priorities
  actor: agent
trigger: '"Business owner wants to grow revenue but doesn''t know which lever to pull, or revenue has plateaued"'
timeSavings: 'Typical run: 4-6 hours, multi-session'
compounding: Each run refines templates and context — 6 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'Revenue plateaued.

  And there are twenty levers you could pull.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Diagnosed growth constraint with targeted 90-day action plan spanning pricing, acquisition, conversion, or product-led growth


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Plan My Next 12 Months — BOB Workflow
  description: Plan My Next 12 Months
  socialImage: https://img.youtube.com/vi/X8zskLUqJAE/maxresdefault.jpg
skillName: pb-plan-my-next-12-months
youtubeId: X8zskLUqJAE
published: '2026-08-01'
privacy: public
title: Plan My Next 12 Months
thumbnail: https://img.youtube.com/vi/X8zskLUqJAE/maxresdefault.jpg
subtitle: 12-Month Business Operating Plan with OKRs, milestones, financial model, market sizing, and a decision filter
inputs:
- label: Client name and industry
  icon: 🏢
- label: Current annual revenue and growth rate
  icon: 📋
- label: Where the business should be in 12 months (vision)
  icon: 🏢
- label: Top 3 constraints (time, budget, team, market, etc.)
  icon: 💰
- label: Key strategic questions or decisions pending
  icon: 📋
outputs:
- label: 12-Month Plan.md
  icon: 🗺️
- label: Annual OKRs.md
  icon: 📋
- label: Financial Model.xlsx
  icon: 💰
- label: TAM-SAM-SOM.md
  icon: 📋
- label: Decision Filter.md
  icon: 📋
- label: Branded Report.pdf
  icon: 📊
steps:
- label: vault-preflight → verify client context completeness and flag blocking gaps before proceeding
  actor: agent
- label: business-baseline → map current business model, growth constraints, and strategic position
  actor: agent
- label: Review baseline — confirm current state, define 12-month vision, and declare top 3 constraints
  actor: human
- label: strategy-frameworks → define strategic direction with where-to-play and how-to-win choices
  actor: agent
- label: market-sizing-analysis → size target market opportunities with TAM/SAM/SOM
  actor: agent
- label: startup-financial-modeling → build 12-month financial model with base, optimistic, and conservative scenarios
  actor: agent
- label: okr-frameworks → set annual OKRs with quarterly milestones and a decision filter for saying yes/no
  actor: agent
- label: business-reporting → consolidate all outputs into a single 12-Month Business Operating Plan
  actor: agent
- label: pdf-report → generate branded PDF of the 12-Month Business Operating Plan with strategy, financials, OKRs, and market sizing
  actor: agent
trigger: '"Business owner wants a 12-month operating plan with strategic direction, OKRs, financial projections, and market context"'
timeSavings: 'Typical run: 3-5 hours, multi-session'
compounding: Each run refines templates and context — 8 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'A year is twelve months.

  Most plans stop being real by March.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---

12-Month Business Operating Plan with OKRs, milestones, financial model, market sizing, and a decision filter


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

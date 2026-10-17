---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Adversarial PMF Review — BOB Workflow
  description: Adversarial PMF Review
  socialImage: https://img.youtube.com/vi/SgORrl_1Uqw/maxresdefault.jpg
skillName: pb-adversarial-pmf-review
youtubeId: SgORrl_1Uqw
published: '2026-08-01'
privacy: public
title: Adversarial PMF Review
thumbnail: https://img.youtube.com/vi/SgORrl_1Uqw/maxresdefault.jpg
subtitle: Honest PMF assessment with scored dimensions, identified weaknesses, and concrete next actions
inputs:
- label: 'Current metrics: MRR/ARR, monthly churn %, NPS score, organic acquisition %'
  icon: 📊
- label: Sean Ellis test result if available ("How would you feel if you could no longer use this product?" — % answering "very disappointed")
  icon: 📦
- label: Top 3 reasons customers buy (from sales calls or surveys)
  icon: 🎙️
- label: Top 3 reasons customers churn or don't buy
  icon: 📋
- label: Competitor names customers mention
  icon: 👤
outputs:
- label: Boardroom Transcript.md
  icon: 🎙️
- label: PMF Scorecard.md
  icon: 📊
- label: Top 3 Gap List.md
  icon: 📋
- label: Action Plan.md
  icon: 🗺️
steps:
- label: Gather PMF metrics — collect retention rate, churn, MRR/ARR, NPS, organic acquisition %, referral rate, switching cost signals
  actor: human
- label: ask-boardroom → configure 5 PMF-adversarial advisors and run the debate
  actor: agent
- label: Review board output — read position papers, rebuttals, and vote tally
  actor: human
- label: Score PMF dimensions from board debate into a structured scorecard
  actor: agent
- label: Review scorecard and identify top 3 PMF gaps to address
  actor: human
- label: decision-frameworks → create action plan for closing the top PMF gap
  actor: agent
trigger: '"When questioning whether the business has real product-market fit, or preparing for investor/board scrutiny on PMF"'
timeSavings: 'Typical run: 1-2 hours, single session'
compounding: Each run refines templates and context — 3 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'You think you have product-market fit.

  Nobody has ever tried to prove you wrong.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---

Honest PMF assessment with scored dimensions, identified weaknesses, and concrete next actions


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

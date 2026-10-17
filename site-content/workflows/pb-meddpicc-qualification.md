---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Meddpicc Qualification — BOB Workflow
  description: MEDDPICC Qualification
  socialImage: https://img.youtube.com/vi/RcbDeI_rLos/maxresdefault.jpg
skillName: pb-meddpicc-qualification
youtubeId: RcbDeI_rLos
published: '2026-08-01'
privacy: public
title: MEDDPICC Qualification
thumbnail: https://img.youtube.com/vi/RcbDeI_rLos/maxresdefault.jpg
subtitle: All 8 MEDDPICC components scored, gaps identified with action plan, and deal go/no-go decision made
inputs:
- label: Deal name and estimated value
  icon: 👤
- label: Current sales stage (Discovery / Evaluation / Proposal / Negotiation)
  icon: 📄
- label: All known contacts and their roles
  icon: 👤
- label: Meeting notes, emails, and prior discovery outputs
  icon: 📧
- label: Known competitors (if any)
  icon: 📋
- label: Procurement requirements (if known)
  icon: 📋
outputs:
- label: MEDDPICC Scorecard.md
  icon: 📊
- label: Buying Committee.md
  icon: 📋
- label: Gap Analysis.md
  icon: 📊
- label: Go/No-Go Decision.md
  icon: 📋
- label: Action Plan.md
  icon: 🗺️
steps:
- label: vault-preflight → verify client context completeness, flag missing intelligence before proceeding
  actor: agent
- label: research-company + prospect-audit → deep company research, competitive landscape, financial health, technology stack
  actor: agent
- label: 'decision-maker-mapper → map full buying committee: economic buyer, technical evaluators, end users, procurement, champion candidates'
  actor: agent
- label: consultative-selling → generate MEDDPICC qualification scorecard from available intelligence, flag gaps requiring discovery
  actor: agent
- label: Review scorecard, identify which components need direct discovery from prospect contacts
  actor: human
- label: Conduct targeted discovery conversations to fill MEDDPICC gaps — focus on Paper Process, Competition, and Economic Buyer access
  actor: human
- label: meeting-intelligence → extract new MEDDPICC evidence from conversation notes, update component scores
  actor: agent
- label: consultative-selling → re-score all 8 components, generate gap analysis with specific actions per weak component
  actor: agent
- label: 'Review updated scores, make go/no-go decision: pursue aggressively, address gaps, nurture, or disqualify'
  actor: human
trigger: '"Active deal needs rigorous qualification — multiple stakeholders, formal procurement, or competitive evaluation in play"'
timeSavings: 'Typical run: Ongoing across deal lifecycle — initial qualification 2-3 hours, weekly updates 30 minutes'
compounding: Each run refines templates and context — 6 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'The deal looks good.

  Ask eight questions and it usually isn''t.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

All 8 MEDDPICC components scored, gaps identified with action plan, and deal go/no-go decision made


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

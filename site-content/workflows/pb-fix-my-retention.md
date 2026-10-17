---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Fix My Retention
  description: Fix My Retention — diagnose at-risk clients and save them
  socialImage: https://img.youtube.com/vi/LnGrEYwrsMg/maxresdefault.jpg
skillName: pb-fix-my-retention
youtubeId: LnGrEYwrsMg
published: '2026-06-29'
privacy: public
title: Fix My Retention — diagnose at-risk clients and save them
thumbnail: https://img.youtube.com/vi/LnGrEYwrsMg/maxresdefault.jpg
subtitle: Diagnosed root cause of the at-risk relationship + a 30-day save plan with specific touchpoints, decisions, and an explicit save/let-go recommendation
inputs:
- label: Client name and `client-id`
  icon: 🏢
- label: 'What changed (specific signals: late payment, missed meetings, NPS drop, escalation, executive turnover)'
  icon: 🎙️
- label: Last positive milestone date
  icon: 📅
- label: Contract renewal date (or rolling)
  icon: 📋
- label: Stakes — revenue at risk, strategic importance, reference value
  icon: 📋
outputs:
- label: Client Health Report — root-cause diagnosis with evidence
  icon: 🏢
- label: 30-Day Save Plan — specific touchpoints, asks, and decisions
  icon: 📦
- label: Save/Let-Go Recommendation — explicit go/no-go with rationale
  icon: 📋
- label: Followup TaskNotes for each save-plan action
  icon: 🎙️
steps:
- label: vault-preflight → verify client context completeness and flag blocking gaps before proceeding
  actor: agent
- label: client-health-tracker → aggregate NPS/CSAT/feedback/deal-activity signals into a current health snapshot
  actor: agent
- label: retention-check → run structured client check-in framework against the snapshot to surface root cause hypotheses
  actor: agent
- label: issue-triage → classify each surfaced issue by severity and SLA — separate "fix-now" from "watch" from "let-go-trigger"
  actor: agent
- label: Review root-cause diagnosis — confirm or correct the hypothesis based on owner's lived context
  actor: human
- label: consultative-selling → frame the save conversation using the appropriate methodology (Gap Selling for diagnosed issues; Challenger for re-framing relationship value; SPICED for situation-pain-impact-critical-decision)
  actor: agent
- label: Decision — save or let go? Based on diagnosis, owner makes the explicit go/no-go call. Save means committing to the 30-day plan; let-go means transitioning the client gracefully
  actor: human
- label: Review proposed save-plan financial commitments (discounts, credits, scope changes) before pdf-report drafts the document — terms-review gate
  actor: human
- label: Approve plan and assign owners — convert each save-plan action to a TaskNote with a specific owner and date
  actor: human
trigger: '"Business owner is losing or about to lose a key client; retention is dropping; renewals declining; client health flagged"'
timeSavings: 'Typical run: 2-4 hours, multi-session'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'The client has gone quiet.

  You''ll find out why when they leave.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Diagnoses an at-risk client and produces a 30-day save plan with an honest save-or-let-go call.

More at brn.cx

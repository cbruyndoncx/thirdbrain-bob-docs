---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Monday CEO Workflow — BOB Workflow
  description: Monday CEO Workflow
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-monday-ceo-workflow
youtubeId: ''
published: ''
privacy: unlisted
title: Monday CEO Workflow
thumbnail: ''
subtitle: KPIs reviewed with 13-week trends, open decisions analyzed and journaled, weekly priorities set, decision-log files written, KPI history updated
inputs:
- label: Week start date (Monday's date)
  icon: 📅
- label: Any decisions to add to the queue before executing
  icon: 📋
- label: Focus areas for review (optional — defaults to all KPI domains)
  icon: 🌐
outputs: []
steps:
- label: SCAN — Read `ceo_review_config.md`, all KPI files, `kpi_history.json` (last 13 weeks), `decision_journal.md` (last entry), and query TaskNotes tagged `#queue/decision` and `#queue/ceo-review`.
    Compute KPI domain statuses (green/amber/red).
  actor: agent
- label: 'PRESENT & COLLECT — Show Monday briefing: KPI dashboard with week-on-week delta, open decision queue (N items), triggered review dates from decision journal, CEO-flagged items. Ask: "Any decisions
    to add or remove?" Accept additions before executing.'
  actor: human
- label: 'business-reporting — CEO review: KPI vs targets, 13-week trend from `kpi_history.json`, pipeline health from deal notes, client health summary, domain status changes since last week. Output: one-page
    CEO review note.'
  actor: agent
- label: 'decision-frameworks or ask-boardroom — For each `#queue/decision` TaskNote, run structured analysis: frame the decision, apply relevant framework (expected value, pre-mortem, reversibility), output
    recommendation + rationale. Steps 3 and 4 run in parallel (no dependency).'
  actor: agent
- label: 'JOURNAL + PRIORITIES — Append entry to `decision_journal.md`: decisions made, deferred, rationale, review dates. Create individual `decision-log` notes in `20-COMPANY/02-DECISIONS/` for each analyzed
    decision. Extract top 3 weekly priorities from review + decision outputs.'
  actor: agent
- label: WRITEBACK — Append this week's snapshot to `kpi_history.json`. Mark analyzed `#queue/decision` TaskNotes as done (link to decision-log output). Create/update `#weekly-priority` TaskNotes for top
    3 priorities. If review surfaced issues, create new `#queue/decision` TaskNotes for next week.
  actor: agent
trigger: '"Every Monday or ''run my Monday CEO review'' — weekly strategic operating grip"'
timeSavings: 'Typical run: 5 min input + 15-20 min execution'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'It''s Monday.

  The numbers are somewhere. The decisions are nowhere.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---



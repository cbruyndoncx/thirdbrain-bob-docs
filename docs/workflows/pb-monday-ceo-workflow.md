---
title: Monday CEO Workflow
---

# Monday CEO Workflow

*KPIs reviewed with 13-week trends, open decisions analyzed and journaled, weekly priorities set, decision-log files written, KPI history updated*

> It's Monday.
> The numbers are somewhere. The decisions are nowhere.

| | |
|---|---|
| **Area** | Strategy |
| **Time savings** | Typical run: 5 min input + 15-20 min execution |
| **Try it** | "Every Monday or 'run my Monday CEO review' — weekly strategic operating grip" |
| **Compounding** | Each run refines templates and context — 5 automated steps improve with accumulated data |
| **Frequency** | Per trigger event |

## Inputs

- 📅 Week start date (Monday's date)
- 📋 Any decisions to add to the queue before executing
- 🌐 Focus areas for review (optional — defaults to all KPI domains)

## What BOB does

1. SCAN — Read `ceo_review_config.md`, all KPI files, `kpi_history.json` (last 13 weeks), `decision_journal.md` (last entry), and query TaskNotes tagged `#queue/decision` and `#queue/ceo-review`. Compute KPI domain statuses (green/amber/red).
2. PRESENT & COLLECT — Show Monday briefing: KPI dashboard with week-on-week delta, open decision queue (N items), triggered review dates from decision journal, CEO-flagged items. Ask: "Any decisions to add or remove?" Accept additions before executing.
3. business-reporting — CEO review: KPI vs targets, 13-week trend from `kpi_history.json`, pipeline health from deal notes, client health summary, domain status changes since last week. Output: one-page CEO review note.
4. decision-frameworks or ask-boardroom — For each `#queue/decision` TaskNote, run structured analysis: frame the decision, apply relevant framework (expected value, pre-mortem, reversibility), output recommendation + rationale. Steps 3 and 4 run in parallel (no dependency).
5. JOURNAL + PRIORITIES — Append entry to `decision_journal.md`: decisions made, deferred, rationale, review dates. Create individual `decision-log` notes in `20-COMPANY/02-DECISIONS/` for each analyzed decision. Extract top 3 weekly priorities from review + decision outputs.
6. WRITEBACK — Append this week's snapshot to `kpi_history.json`. Mark analyzed `#queue/decision` TaskNotes as done (link to decision-log output). Create/update `#weekly-priority` TaskNotes for top 3 priorities. If review surfaced issues, create new `#queue/decision` TaskNotes for next week.


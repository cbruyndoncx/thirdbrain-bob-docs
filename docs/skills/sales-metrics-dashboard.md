---
description: Treat sales as a math problem. Know your numbers, find the leaks, fix the right stage.
title: sales-metrics-dashboard
---

# sales-metrics-dashboard

Treat sales as a math problem. Know your numbers, find the leaks, fix the right stage.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Sales] |

Builds daily activity KPI dashboards, models funnel conversion rates between stages, calculates sales velocity, and identifies where deals are dying.

## How you ask

- “Build me a sales metrics dashboard for this week”
- “I need to close $100K this month — what's my daily outreach target?”
- “My close rate is 15% — what's wrong and how do I fix it?”
- “Where is my funnel leaking? Here are my numbers: [paste stats]”
- “Generate a weekly sales report from my pipeline data”

## Inputs

- kpi_registry — Canonical KPI ids and thresholds. Bind to existing ids rather than defining parallel metrics that drift from the weekly KPI loop.
- pipeline-data — Current opportunities, stages, values, dates, owners, activities, and reporting scope.
- reporting-period — Existing dashboard plus new period pipeline, activity, conversion, and revenue observations.
- funnel-metrics — Stage counts, conversion rates, cycle time, targets, and comparison period.
- revenue-target — Revenue goal, average deal size, stage conversions, working days, and current capacity.

## Outputs

- activity-targets (markdown)
- funnel-audit (markdown)
- sales-dashboard (markdown)
- sales-weekly (markdown)
- {scope.sales}/activity-targets-{date}.md
- {scope.sales}/funnel-audit-{date}.md
- {scope.sales}/sales-dashboard-{date}.md
- {scope.sales}/sales-weekly-{date}.md


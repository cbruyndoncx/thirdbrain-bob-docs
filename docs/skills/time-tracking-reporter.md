---
description: Transform raw time logs into clear productivity reports with utilization rates, project breakdowns, and actionable insights.
title: time-tracking-reporter
---

# time-tracking-reporter

Transform raw time logs into clear productivity reports with utilization rates, project breakdowns, and actionable insights.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | business |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Finance Manager] |

Transforms time logs into productivity reports with utilization rates, project breakdowns, and trend analysis.

## How you ask

- “Generate a productivity report from my Toggl export”
- “Analyze my time logs and show utilization rates”
- “Break down my billable hours by project for this month”
- “Create a time tracking report from this CSV file”

## Inputs

- request — The report scope, period, and the raw time-log data (or its source format) — triggers the full report with all components.
- request — The report scope and period, and the raw time-log data — triggers topline totals and utilization only.
- request — The raw time-log data and any known data-quality concerns — triggers normalization before totals are calculated.

## Outputs

- Full productivity report — executive summary, utilization split, project/client breakdown, daily/weekly distribution, and 3-5 insights with recommendations. Falls back to the inbox (`me.inbox`) or scratch space (`output.scratch`) when the management folder isn't available.
- Normalized time-log rows plus the list of data-quality issues found (crossed-midnight entries, overlaps, zero-duration rows, unallocated codes) and how each was resolved, ready to feed the `full-report` or `summary` route.
- Topline tracked hours and utilization rate only, without the project/client or daily/weekly breakdowns. Falls back to the inbox (`me.inbox`) or scratch space (`output.scratch`) when the management folder isn't available.
- {company.reports}/time-report-{YYYY-MM-DD}.md


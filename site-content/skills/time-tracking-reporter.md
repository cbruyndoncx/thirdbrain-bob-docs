---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: time-tracking-reporter — ThirdBrain BOB skill
  description: Transform raw time logs into clear productivity reports with utilization rates, project breakdowns, and actionable insights.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: time-tracking-reporter
catLabel: business
area: strategy
desc: Transforms time logs into productivity reports with utilization rates, project breakdowns, and trend analysis.
summary: Transform raw time logs into clear productivity reports with utilization rates, project breakdowns, and actionable insights.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- request — The report scope, period, and the raw time-log data (or its source format) — triggers the full report with all components.
- request — The report scope and period, and the raw time-log data — triggers topline totals and utilization only.
- request — The raw time-log data and any known data-quality concerns — triggers normalization before totals are calculated.
outputs:
- Full productivity report — executive summary, utilization split, project/client breakdown, daily/weekly distribution, and 3-5 insights with recommendations. Falls back to the inbox (`me.inbox`) or scratch space (`output.scratch`) when the management folder isn't available.
- Normalized time-log rows plus the list of data-quality issues found (crossed-midnight entries, overlaps, zero-duration rows, unallocated codes) and how each was resolved, ready to feed the `full-report` or `summary` route.
- Topline tracked hours and utilization rate only, without the project/client or daily/weekly breakdowns. Falls back to the inbox (`me.inbox`) or scratch space (`output.scratch`) when the management folder isn't available.
- '{company.reports}/time-report-{YYYY-MM-DD}.md'
prompts:
- Generate a productivity report from my Toggl export
- Analyze my time logs and show utilization rates
- Break down my billable hours by project for this month
- Create a time tracking report from this CSV file
---

---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: sales-metrics-dashboard — ThirdBrain BOB skill
  description: Treat sales as a math problem. Know your numbers, find the leaks, fix the right stage.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: sales-metrics-dashboard
catLabel: sales
area: sales
desc: Builds daily activity KPI dashboards, models funnel conversion rates between stages, calculates sales velocity, and identifies where deals are dying.
summary: Treat sales as a math problem. Know your numbers, find the leaks, fix the right stage.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- kpi_registry — Canonical KPI ids and thresholds. Bind to existing ids rather than defining parallel metrics that drift from the weekly KPI loop.
- pipeline-data — Current opportunities, stages, values, dates, owners, activities, and reporting scope.
- reporting-period — Existing dashboard plus new period pipeline, activity, conversion, and revenue observations.
- funnel-metrics — Stage counts, conversion rates, cycle time, targets, and comparison period.
- revenue-target — Revenue goal, average deal size, stage conversions, working days, and current capacity.
outputs:
- activity-targets (markdown)
- funnel-audit (markdown)
- sales-dashboard (markdown)
- sales-weekly (markdown)
- '{scope.sales}/activity-targets-{date}.md'
- '{scope.sales}/funnel-audit-{date}.md'
- '{scope.sales}/sales-dashboard-{date}.md'
- '{scope.sales}/sales-weekly-{date}.md'
prompts:
- Build me a sales metrics dashboard for this week
- I need to close $100K this month — what's my daily outreach target?
- My close rate is 15% — what's wrong and how do I fix it?
- 'Where is my funnel leaking? Here are my numbers: [paste stats]'
- Generate a weekly sales report from my pipeline data
---

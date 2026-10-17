---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: kpi-dashboard-design — ThirdBrain BOB skill
  description: 'Use this skill to define the dashboard before anyone builds it: what decisions it supports, which metrics belong, and how the view should be structured.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: kpi-dashboard-design
catLabel: product-management
area: strategy
desc: Designs KPI dashboards, selects meaningful metrics, and applies visualization best practices for real-time monitoring.
summary: 'Use this skill to define the dashboard before anyone builds it: what decisions it supports, which metrics belong, and how the view should be structured.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager, Operations Manager, Finance Manager]'
inputs:
- kpi_registry — Canonical KPI ids and thresholds. Bind to existing ids rather than defining parallel metrics that drift from the weekly KPI loop.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- kpi-dashboard-design (markdown)
- kpi-dashboard-design-company (markdown)
- '{client.knowledge-base.product}/kpi-dashboard-design-{YYYY-MM-DD}.md'
- '{company.knowledge-base.product}/kpi-dashboard-design-{YYYY-MM-DD}.md'
prompts:
- Design a KPI dashboard for our SaaS metrics
- Select meaningful metrics for our executive dashboard
- Create a real-time monitoring dashboard for our operations
- Apply visualization best practices to our analytics board
---

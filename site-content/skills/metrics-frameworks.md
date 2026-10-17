---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: metrics-frameworks — ThirdBrain BOB skill
  description: Selects metric frameworks, defines precise KPIs, distinguishes vanity from actionable metrics, sets targets, and recommends review cadences. Use when user menti
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: metrics-frameworks
catLabel: product-management
area: strategy
desc: Selects metric frameworks, defines precise KPIs, distinguishes vanity from actionable metrics, sets targets, and recommends review cadences.
summary: Selects metric frameworks, defines precise KPIs, distinguishes vanity from actionable metrics, sets targets, and recommends review cadences. Use when user mentions 'north star metric,' 'AARRR,' 'pirate metrics,' 'vanity metrics,' 'product analytics.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Marketing, Product Manager]'
inputs:
- kpi_registry — Canonical KPI ids and thresholds. Bind to existing ids rather than defining parallel metrics that drift from the weekly KPI loop.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- metrics-frameworks (markdown)
- metrics-frameworks-company (markdown)
- '{client.knowledge-base.product}/metrics-frameworks-{YYYY-MM-DD}.md'
- '{company.knowledge-base.product}/metrics-frameworks-{YYYY-MM-DD}.md'
prompts:
- Define our north star metric for the product
- Set up AARRR pirate metrics for our startup
- Distinguish vanity metrics from actionable ones in our dashboard
- Create a metrics review cadence for our team
---

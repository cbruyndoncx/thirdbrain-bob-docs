---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: startup-financial-modeling — ThirdBrain BOB skill
  description: Builds 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for startups. Use when user needs a spread
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: startup-financial-modeling
catLabel: product-management
area: strategy
desc: Builds 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for startups.
summary: Builds 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for startups. Use when user needs a spreadsheet-ready financial model or mentions 'financial model,' 'burn rate,' 'runway,' 'cash flow,' or 'financial projections.' For market sizing (TAM/SAM/SOM), see market-sizing-analysis. For broader competitive and strategic analysis, see startup-analyst.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Finance Manager]'
inputs:
- request — The business model, modeling horizon, and known assumptions — triggers a complete revenue, cost, cash-flow, and 3-scenario model.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The runway or funding-timing question and the known cash position — triggers a cash flow, burn, and runway analysis.
- request — What is known and what is sparse — triggers a documented assumption set with provisional outputs and flags for what must be verified next.
outputs:
- Current cash, monthly burn, runway in months, and the funding-need date, traceable to the stated cash and expense assumptions.
- Documented assumption set, each entry marked placeholder or confirmed, with provisional outputs and the follow-up verification needed before it can be treated as a full model.
- Full model — key assumptions, 3-year summary, unit economics, cash position, and scenario comparison across conservative, base, and optimistic cases.
- '{scope.knowledge-base.product}/startup-financial-modeling-{YYYY-MM-DD}.md'
prompts:
- Build a 3-year financial model for our SaaS startup
- Project our burn rate and runway for the next 18 months
- Create a cash flow analysis with scenario planning
- Model our revenue growth with different pricing assumptions
---

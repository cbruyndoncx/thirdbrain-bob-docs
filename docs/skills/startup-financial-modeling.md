---
description: Builds 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for startups. Use when user needs a spreadsheet-ready financial model or mentions 'financial model,' 'burn rate,' 'runway,' 'cash flow,' or 'financial projections.' For market sizing (TAM/SAM/SOM), see market-sizing-analysis. For broader competitive and strategic analysis, see startup-analyst.
title: startup-financial-modeling
---

# startup-financial-modeling

Builds 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for startups. Use when user needs a spreadsheet-ready financial model or mentions 'financial model,' 'burn rate,' 'runway,' 'cash flow,' or 'financial projections.' For market sizing (TAM/SAM/SOM), see market-sizing-analysis. For broader competitive and strategic analysis, see startup-analyst.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Finance Manager] |

Builds 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for startups.

## How you ask

- “Build a 3-year financial model for our SaaS startup”
- “Project our burn rate and runway for the next 18 months”
- “Create a cash flow analysis with scenario planning”
- “Model our revenue growth with different pricing assumptions”

## Inputs

- request — The business model, modeling horizon, and known assumptions — triggers a complete revenue, cost, cash-flow, and 3-scenario model.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The runway or funding-timing question and the known cash position — triggers a cash flow, burn, and runway analysis.
- request — What is known and what is sparse — triggers a documented assumption set with provisional outputs and flags for what must be verified next.

## Outputs

- Current cash, monthly burn, runway in months, and the funding-need date, traceable to the stated cash and expense assumptions.
- Documented assumption set, each entry marked placeholder or confirmed, with provisional outputs and the follow-up verification needed before it can be treated as a full model.
- Full model — key assumptions, 3-year summary, unit economics, cash position, and scenario comparison across conservative, base, and optimistic cases.
- {scope.knowledge-base.product}/startup-financial-modeling-{YYYY-MM-DD}.md


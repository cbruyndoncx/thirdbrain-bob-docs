---
description: Design the right team shape, hiring sequence, and compensation logic for an early-stage startup without copying a later-stage org chart.
title: team-composition-analysis
---

# team-composition-analysis

Design the right team shape, hiring sequence, and compensation logic for an early-stage startup without copying a later-stage org chart.

| | |
|---|---|
| **Area** | People |
| **Category** | human resources |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, HR Manager] |

Designs startup org structures, hiring plans, compensation assumptions, equity ranges, and headcount budgets for early-stage teams.

## How you ask

- “team structure”
- “hiring plan”
- “org chart”
- “compensation”
- “headcount planning”

## Inputs

- request — The org-design question — current team shape, the next structural decision, or a specific reporting-line question to resolve.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company profile — stage, funding, and current team, used to anchor the structure to the stage rather than a later-stage template.
- icp — ICP — who the team serves; shapes which go-to-market or delivery functions the structure must cover.
- request — The hiring-sequencing question — which roles, in what order, and against which trigger or constraint.
- profile — Company profile — stage, funding, and current team, used to judge which triggers are close enough to act on.
- icp — ICP — who the team serves; shapes which customer-facing or delivery hires are triggered by growing demand.
- request — The compensation or equity question — which role, which geography, and whether the ask is a salary range, an equity range, or fully-loaded cost.
- profile — Company profile — funding stage and dilution context, used to place the equity range in `compensation_equity_benchmarks.md` correctly.
- request — The scope of the combined brief — the decision it needs to support and any constraint that should override the default benchmarks.
- profile — Company profile — stage, funding, and current team for composition, sequencing, and compensation design.
- icp — ICP — who the team serves; shapes go-to-market roles across the structure and hiring sequence.

## Outputs

- Combined brief — team structure, hiring sequence, compensation and equity assumptions, budget impact, and main risks — in one document.
- Hiring order with each role's trigger, and the full-time versus contract versus fractional call for each.
- Recommended team structure and reporting lines, tied to the stated stage and business goal.
- Salary and equity ranges with geography and dilution-stage assumptions named, and fully-loaded cost shown with its multiplier.
- {scope.knowledge-base.product}/team-composition-analysis-{YYYY-MM-DD}.md


---
description: Selects metric frameworks, defines precise KPIs, distinguishes vanity from actionable metrics, sets targets, and recommends review cadences. Use when user mentions 'north star metric,' 'AARRR,' 'pirate metrics,' 'vanity metrics,' 'product analytics.'
title: metrics-frameworks
---

# metrics-frameworks

Selects metric frameworks, defines precise KPIs, distinguishes vanity from actionable metrics, sets targets, and recommends review cadences. Use when user mentions 'north star metric,' 'AARRR,' 'pirate metrics,' 'vanity metrics,' 'product analytics.'

- **Area:** Strategy
- **Category:** product management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Head of Marketing, Product Manager

Selects metric frameworks, defines precise KPIs, distinguishes vanity from actionable metrics, sets targets, and recommends review cadences.

## How you ask

- “Define our north star metric for the product”
- “Set up AARRR pirate metrics for our startup”
- “Distinguish vanity metrics from actionable ones in our dashboard”
- “Create a metrics review cadence for our team”

## Inputs

- kpi_registry — Canonical KPI ids and thresholds. Bind to existing ids rather than defining parallel metrics that drift from the weekly KPI loop.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- metrics-frameworks (markdown)
- metrics-frameworks-company (markdown)
- {client.knowledge-base.product}/metrics-frameworks-{YYYY-MM-DD}.md
- {company.knowledge-base.product}/metrics-frameworks-{YYYY-MM-DD}.md


---
description: 'Use this skill to define the dashboard before anyone builds it: what decisions it supports, which metrics belong, and how the view should be structured.'
title: kpi-dashboard-design
---

# kpi-dashboard-design

Use this skill to define the dashboard before anyone builds it: what decisions it supports, which metrics belong, and how the view should be structured.

- **Area:** Strategy
- **Category:** product management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Product Manager, Operations Manager, Finance Manager

Designs KPI dashboards, selects meaningful metrics, and applies visualization best practices for real-time monitoring.

## How you ask

- “Design a KPI dashboard for our SaaS metrics”
- “Select meaningful metrics for our executive dashboard”
- “Create a real-time monitoring dashboard for our operations”
- “Apply visualization best practices to our analytics board”

## Inputs

- kpi_registry — Canonical KPI ids and thresholds. Bind to existing ids rather than defining parallel metrics that drift from the weekly KPI loop.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- kpi-dashboard-design (markdown)
- kpi-dashboard-design-company (markdown)
- {client.knowledge-base.product}/kpi-dashboard-design-{YYYY-MM-DD}.md
- {company.knowledge-base.product}/kpi-dashboard-design-{YYYY-MM-DD}.md


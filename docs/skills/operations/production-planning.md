---
description: Analyze manufacturing operations data from Odoo MRP or ERPNext Manufacturing. Generates reports on production order status, work center capacity and OEE, BOM structure and cost, production scheduling, and scrap/waste trends.
title: production-planning
---

# production-planning

Analyze manufacturing operations data from Odoo MRP or ERPNext Manufacturing. Generates reports on production order status, work center capacity and OEE, BOM structure and cost, production scheduling, and scrap/waste trends.

- **Area:** Operations
- **Category:** operations
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Analyze manufacturing orders, BOM structures, work center capacity, OEE metrics, and scrap rates.

## How you ask

- “Show me the status of all manufacturing orders for Bobbolt over the last 30 days”
- “Which work centers are bottlenecks right now? Give me the capacity and OEE breakdown”
- “Explode the BOM for product SKU-4200 and flag any single-source components”
- “Build a two-week production schedule from the open manufacturing orders”
- “What are our scrap rates by work center for the last quarter, and where is waste trending up?”

## Inputs

- data_source — CSV path, inline data, or 'mcp' for live query
- date_range — Reporting period (default: last 30 days)
- offerings — Offerings catalogue — what we produce; anchors product-level commentary.
- bom_reference — Specific BOM reference to analyze (omit for all active BOMs)
- horizon — Scheduling horizon (default: 2 weeks)
- date_range — Reporting period (default: last 90 days)

## Outputs

- BOM tree, cost rollup, single-source flags
- Gantt-style schedule with critical path
- MO pipeline report with state breakdown and completion rates
- Scrap rates with trends by product, work center, and period
- Utilization and OEE per work center with bottleneck flags
- {client.deliverables.production}/bom_analysis.md
- {client.deliverables.production}/capacity_report.md
- {client.deliverables.production}/mo_status_report.md
- {client.deliverables.production}/production_schedule.md
- {client.deliverables.production}/scrap_analysis.md


---
description: Track the full order lifecycle from receipt through fulfillment. Surface bottlenecks, flag at-risk orders, analyze return patterns, and forecast demand — all from ERP data or simple CSV dumps.
title: order-management
---

# order-management

Track the full order lifecycle from receipt through fulfillment. Surface bottlenecks, flag at-risk orders, analyze return patterns, and forecast demand — all from ERP data or simple CSV dumps.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Tracks order lifecycle from receipt to fulfillment, analyzes fulfillment performance, and generates order operations reports.

## How you ask

- “Generate an order status dashboard for Acme Corp”
- “What's causing fulfillment delays for our biggest client?”
- “Show me all overdue orders with revenue at risk”
- “Analyze return patterns for Q1 — what products have the highest return rate?”
- “Forecast order volume for next quarter based on the last 12 months”

## Inputs

- source (Order Status) — Order data CSV/JSON or MCP query parameters
- source (Fulfillment Analysis) — Fulfillment data (stock.picking/Delivery Note or CSV)
- source (Backlog Review) — Open orders data
- source (Returns Analysis) — Return data (reverse pickings or CSV)
- source (Demand Forecast) — Historical order data (6+ months recommended)

## Outputs

- backlog-report (markdown)
- demand-forecast (markdown)
- fulfillment-report (markdown)
- order-status-report (markdown)
- returns-report (markdown)
- {client.deliverables.orders}/backlog_report_{YYYY-MM-DD}.md
- {client.deliverables.orders}/demand_forecast_{YYYY-MM-DD}.md
- {client.deliverables.orders}/fulfillment_analysis_{YYYY-MM-DD}.md
- {client.deliverables.orders}/order_status_{YYYY-MM-DD}.md
- {client.deliverables.orders}/returns_analysis_{YYYY-MM-DD}.md


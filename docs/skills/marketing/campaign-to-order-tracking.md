---
description: Connect marketing campaign spend to qualified orders and revenue. Measures attribution, ROI, and channel effectiveness from spreadsheet data — no CRM integration or BI tooling required.
title: campaign-to-order-tracking
---

# campaign-to-order-tracking

Connect marketing campaign spend to qualified orders and revenue. Measures attribution, ROI, and channel effectiveness from spreadsheet data — no CRM integration or BI tooling required.

- **Area:** Marketing
- **Category:** marketing analytics
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing

Maps uploaded campaign/spend and order CSV or spreadsheet exports to qualified orders and revenue.

## How you ask

- “Map last quarter's campaign spend to the orders we closed”
- “Which of our channels has the best ROI — paid search, email, or LinkedIn?”
- “Show me where leads are dropping out in our funnel for each campaign”
- “Build an attribution report using last-touch for Q1 2025”
- “Compare channel performance for the past 90 days”

## Inputs

- campaign-data — Spreadsheet or CSV with at minimum: campaign name, channel, spend, date range
- order-data — Spreadsheet or CSV with at minimum: order ID, order date, revenue, lead source or campaign tag
- attribution-model — Attribution model to apply. 'auto' selects last-touch unless user specifies otherwise. See references/attribution_models.md. (last-touch | first-touch | linear | auto)
- campaign-data — Spreadsheet or CSV with campaign name, channel, spend, date range
- order-data — Spreadsheet or CSV with order ID, revenue, and a channel or campaign tag that matches the campaign data
- period — Date range to analyze (e.g. 'Q1 2025', 'last 90 days'). Defaults to full date range in the data.
- funnel-data — Spreadsheet or CSV with stage-level counts per campaign: impressions or clicks, leads generated, qualified leads, orders. At minimum: campaign name, leads, and orders.
- campaign-spend — Separate spend file if not included in funnel data. Required for cost-per-stage metrics.

## Outputs

- attribution-report (markdown)
- channel-comparison (markdown)
- funnel-report (markdown)
- prefer a permanent directory)


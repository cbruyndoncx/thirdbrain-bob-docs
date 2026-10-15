---
description: Transform completed work into clear, professional invoice line items that clients understand and approve without questions.
title: invoice-description
---

# invoice-description

Transform completed work into clear, professional invoice line items that clients understand and approve without questions.

| | |
|---|---|
| **Area** | Finance |
| **Category** | finance |
| **Level** | beginner |
| **Input** | data |
| **Output** | spreadsheet |
| **Setup** | [none] |
| **Roles** | [Finance Manager] |

Converts completed work items into invoice line-item descriptions for QuickBooks or Xero.

## How you ask

- “Convert these task items into invoice line descriptions”
- “Write professional invoice descriptions for this week's work”
- “Turn my time log into client-ready billing summaries”

## Inputs

- client-profile — Client profile — billing entity context.
- source (Raw work items) — Task list, time log, or work summary
- offerings — loaded from your vault context
- profile — loaded from your vault context
- source (Review route) — Existing draft line items to review
- source (Summary route) — Work items and period for billing summary

## Outputs

- invoice (markdown)
- revised-invoice (markdown)
- {client.invoices}/invoice-{client-id}-{YYYY-MM-DD}.md


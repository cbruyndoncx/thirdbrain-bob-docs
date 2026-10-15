---
description: Generate proof of delivery documents, document and escalate delivery problems, and produce delivery performance summaries. Activates at the final mile — after goods leave the warehouse and before customer sign-off is complete.
title: delivery-confirmation
---

# delivery-confirmation

Generate proof of delivery documents, document and escalate delivery problems, and produce delivery performance summaries. Activates at the final mile — after goods leave the warehouse and before customer sign-off is complete.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Records delivery outcomes in the vault, generates proof of delivery documents, and manages customer sign-off.

## How you ask

- “Confirm delivery”
- “Delivery receipt”
- “Proof of delivery”

## Inputs

- delivery_details — Order number, delivery address, items delivered, recipient name, date/time
- condition_notes — Item condition, packaging state, any exceptions noted at handoff
- issue_description — What went wrong: missing items, damage, wrong address, refused delivery, etc.
- order_reference — Order number or delivery reference for the affected shipment
- period — Reporting period (e.g. 'March 2026', 'Q1 2026', 'last 30 days')
- data_source — Source of delivery data: spreadsheet, system export, or manual log

## Outputs

- delivery-report (markdown)
- issue-report (markdown)
- proof-of-delivery (markdown)
- {client.root}/YYYY-MM-{project}/delivery-issue-{order-id}.md
- {client.root}/YYYY-MM-{project}/delivery-receipt-{order-id}.md
- {company.operations}/delivery-report-{YYYY-MM}.md


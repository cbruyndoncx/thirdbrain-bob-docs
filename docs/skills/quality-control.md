---
description: Create and run quality control processes for manufacturing and production using simple checklists and markdown tables — no specialist QMS software required. Covers product inspection, defect tracking, and quality reporting at the shift, batch, or product-line level.
title: quality-control
---

# quality-control

Create and run quality control processes for manufacturing and production using simple checklists and markdown tables — no specialist QMS software required. Covers product inspection, defect tracking, and quality reporting at the shift, batch, or product-line level.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Creates inspection checklists, defect tracking logs, pass/fail documentation, and quality reports for manufacturing and production.

## How you ask

- “Inspect products”
- “Track defects”
- “Quality results”

## Inputs

- product_name — Name or SKU of the product being inspected
- inspection_type — Type of inspection: incoming, in-process, or final (default: final)
- specifications — Key product specs or standards to check against (text, CSV, or file path)
- batch_id — Batch, lot, or production run reference
- product_name — Product name or SKU
- defects — Defects to log (inline description, CSV, or existing log file path to append)
- data_source — Path to defect logs, inline data, or inspection results to summarise
- period — Reporting period (default: last 30 days or all supplied data)
- product_filter — Limit report to a specific product or product family (omit for all)

## Outputs

- Defect log table with severity, category, root cause, disposition, and corrective action fields
- Quality summary with pass/fail rates, top defect categories, trend indicators, and recommendations
- Structured checklist with inspection points, acceptance criteria, pass/fail columns, and inspector sign-off
- {client.deliverables.quality-control}/defect_log_{batch}.md
- {client.deliverables.quality-control}/inspection_checklist_{product}.md
- {client.deliverables.quality-control}/quality_report_{period}.md


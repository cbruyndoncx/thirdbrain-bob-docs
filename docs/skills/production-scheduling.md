---
description: Build production schedules from orders or forecasts, sequence batches to minimize changeover, and check whether planned volumes fit within available work center capacity. Designed for production planners and operations leads who work in spreadsheets and markdown — no MES or ERP connection required.
title: production-scheduling
---

# production-scheduling

Build production schedules from orders or forecasts, sequence batches to minimize changeover, and check whether planned volumes fit within available work center capacity. Designed for production planners and operations leads who work in spreadsheets and markdown — no MES or ERP connection required.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Creates production schedules with work center allocation, batch sequencing, and timeline management.

## How you ask

- “Schedule a production run”
- “Allocate work centers”
- “Sequence batches”

## Inputs

- orders-or-forecast — Order list, forecast data, or production requirements
- offerings — Offerings catalogue — anchors product-level scheduling assumptions.
- batch-list — List of batches with product, quantity, and constraints
- schedule — Existing or proposed production schedule

## Outputs

- capacity-report (markdown)
- prefer a permanent directory)
- schedule (markdown)
- sequence (markdown)


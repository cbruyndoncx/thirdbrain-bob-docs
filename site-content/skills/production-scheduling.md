---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: production-scheduling — ThirdBrain BOB skill
  description: Build production schedules from orders or forecasts, sequence batches to minimize changeover, and check whether planned volumes fit within available work center
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: production-scheduling
catLabel: operations
area: operations
desc: Creates production schedules with work center allocation, batch sequencing, and timeline management.
summary: Build production schedules from orders or forecasts, sequence batches to minimize changeover, and check whether planned volumes fit within available work center capacity. Designed for production planners and operations leads who work in spreadsheets and markdown — no MES or ERP connection required.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- orders-or-forecast — Order list, forecast data, or production requirements
- offerings — Offerings catalogue — anchors product-level scheduling assumptions.
- batch-list — List of batches with product, quantity, and constraints
- schedule — Existing or proposed production schedule
outputs:
- capacity-report (markdown)
- prefer a permanent directory)
- schedule (markdown)
- sequence (markdown)
prompts:
- Schedule a production run
- Allocate work centers
- Sequence batches
---

---
description: The runtime engine of the Owner Operating System. Reads company signals, computes health-domain scores, runs the data-quality gate, identifies the binding constraint, and writes the recommendation back to `CURRENT-STATE.md`.
title: owner-priority-system
---

# owner-priority-system

The runtime engine of the Owner Operating System. Reads company signals, computes health-domain scores, runs the data-quality gate, identifies the binding constraint, and writes the recommendation back to `CURRENT-STATE.md`.

- **Area:** Strategy
- **Category:** business
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder

Turns company state and operating signals into a concise owner priority brief — diagnoses current business state, identifies binding constraint, ranks evidence, sets top…

## How you ask

- “What should I focus on now”
- “What's my biggest problem”
- “Where am I leaking”

## Inputs

- current-state — CURRENT-STATE.md, under the management tree (`company.management`) — prior state for delta comparison
- kpi-registry — KPI-REGISTRY.md, under the management tree (`company.management`) — thresholds and source mappings
- horizon — Planning horizon — weekly sets next-week priorities, monthly sets next-month (weekly | monthly)
- current-state — CURRENT-STATE.md, under the management tree (`company.management`)
- current-state — CURRENT-STATE.md, under the management tree (`company.management`) (must have business_state + binding_constraint set)

## Outputs

- brief (markdown)
- diagnosis (markdown)
- priorities (markdown)
- route (markdown)
- {company.management}/CURRENT-STATE.md
- {company.management}/briefs/{YYYY-MM-DD}_owner_brief.md


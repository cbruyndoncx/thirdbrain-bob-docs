---
description: Create, review, and track purchase requisitions — the first step in the procure-to-pay lifecycle. A PR captures what is needed, why, how much it costs, and who needs to approve it before a purchase order is created.
title: purchase-requisition
---

# purchase-requisition

Create, review, and track purchase requisitions — the first step in the procure-to-pay lifecycle. A PR captures what is needed, why, how much it costs, and who needs to approve it before a purchase order is created.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Creates and manages purchase requisitions — the formal request to buy goods or services.

## How you ask

- “I need to purchase a project management tool for the team, about $500 per year”
- “Review and approve PR-2026-014 for the new office supplies order”
- “Show me a dashboard of all open purchase requisitions and flag anything older than a week”
- “Create a purchase request for consulting services from Acme Corp, estimated at $12,000”

## Inputs

- source (create) — Purchase need description and estimated cost
- source (review) — PR ID and approval decision
- source (dashboard) — Dashboard request with optional filters
- all — loaded from your vault context
- profile — loaded from your vault context

## Outputs

- pr-dashboard (markdown)
- purchase-requisition (markdown)
- reviewed-pr (markdown)
- {scope.finance.ap-requisitions}/PR-{YYYY}-{NNN}.md
- {scope.finance.ap-requisitions}/{pr-id}.md
- {scope.finance.ap}/pr_dashboard_{YYYY-MM-DD}.md


---
description: Create, amend, and track purchase orders — the formal commitment to a supplier for goods or services at agreed terms. A PO is the bridge between an approved purchase requisition and supplier delivery/invoicing.
title: purchase-order
---

# purchase-order

Create, amend, and track purchase orders — the formal commitment to a supplier for goods or services at agreed terms. A PO is the bridge between an approved purchase requisition and supplier delivery/invoicing.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager, Finance Manager] |

Creates and manages purchase orders — the formal commitment to buy from a supplier at agreed terms.

## How you ask

- “Create a purchase order for the approved PR from DataSync for the annual SaaS license”
- “Show me the status of all open purchase orders and flag anything overdue”
- “Amend PO-2026-008 to add a second milestone for the additional consulting work”
- “Does this invoice from CloudHost match PO-2026-011? Quick check before I process it”

## Inputs

- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- source (create) — Purchase details or approved PR reference
- existing-orders — loaded from your vault context
- pr-id — loaded from your vault context
- profile — loaded from your vault context
- source (amend) — PO ID and amendment details
- source (status) — Status dashboard request
- source (match) — Invoice details and PO reference

## Outputs

- amended-po (markdown)
- match-report (markdown)
- po-status-dashboard (markdown)
- purchase-order (markdown)
- {scope.finance.ap-orders}/PO-{YYYY}-{NNN}.md
- {scope.finance.ap-orders}/{po-id}.md
- {scope.finance.ap}/match_report_{po-id}.md
- {scope.finance.ap}/po_status_{YYYY-MM-DD}.md


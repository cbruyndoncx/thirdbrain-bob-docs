---
description: 'Manage the final stages of the procure-to-pay lifecycle: confirm service delivery, match supplier invoices against purchase orders, process payments, and close the procurement cycle. Combines delivery acceptance, invoice processing, and payment into a single streamlined workflow for services-oriented SMBs.'
title: order-to-pay
---

# order-to-pay

Manage the final stages of the procure-to-pay lifecycle: confirm service delivery, match supplier invoices against purchase orders, process payments, and close the procurement cycle. Combines delivery acceptance, invoice processing, and payment into a single streamlined workflow for services-oriented SMBs.

- **Area:** Strategy
- **Category:** business
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager, Finance Manager

Manages the final stages of the procure-to-pay lifecycle — service delivery acceptance, 3-way invoice matching (PO vs delivery vs invoice), payment processing, and PO…

## How you ask

- “We received an invoice from Acme Corp for the website redesign project, can you match it against PO-2026-012?”
- “Show me the AP dashboard with all outstanding invoices and what's overdue”
- “The invoice from CloudHost doesn't match the PO amount — flag it as a dispute and draft a response”
- “Mark the delivery for PO-2026-015 as accepted, all three milestones are complete”
- “Close out PO-2026-009, everything has been paid and delivered”

## Inputs

- source (receive) — PO ID and delivery details
- invoices — loaded from your vault context
- po-id — loaded from your vault context
- profile — loaded from your vault context
- source (match-and-process) — Invoice details and PO reference
- source (dispute) — Invoice and PO with discrepancy details
- source (close) — PO ID to close
- source (ap-dashboard) — Dashboard request with optional date filter

## Outputs

- ap-aging-report (markdown)
- closed-po (markdown)
- disputed-invoice (markdown)
- supplier-invoice (markdown)
- updated-po (markdown)
- {scope.finance.ap-invoices}/SI-{YYYY}-{NNN}.md
- {scope.finance.ap-orders}/{po-id}.md
- {scope.finance.ap}/ap_dashboard_{YYYY-MM-DD}.md


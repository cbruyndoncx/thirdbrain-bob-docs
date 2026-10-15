---
description: Collect ongoing supplier performance reviews, build scorecard history, track trends, and flag at-risk vendor relationships. Complements `strategic-sourcing` (one-time evaluation) with a continuous feedback loop for active supplier relationships.
title: supplier-feedback
---

# supplier-feedback

Collect ongoing supplier performance reviews, build scorecard history, track trends, and flag at-risk vendor relationships. Complements `strategic-sourcing` (one-time evaluation) with a continuous feedback loop for active supplier relationships.

- **Area:** Operations
- **Category:** operations
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Ongoing supplier performance tracking — periodic reviews of delivery quality, responsiveness, cost accuracy, and SLA compliance with scorecard history and trend analysis.

## How you ask

- “Run a quarterly performance review for Acme Industrial covering Q1 2026”
- “Show me the performance trend for our packaging supplier over the last four reviews”
- “Compare all logistics suppliers side by side on delivery and responsiveness”
- “Flag any suppliers that are underperforming or overdue for a review”
- “Audit supplier master data for inconsistencies across POs and invoices”

## Inputs

- supplier_id — Supplier under review, matching the folder under the suppliers root (`company.suppliers`)
- period — Review period covered (e.g. 2026-Q2)
- kraljic-matrix — loaded from your vault context
- contact-details — loaded from your vault context
- profile — loaded from your vault context
- supplier_id — Supplier whose review history is to be trended
- periods — How many prior periods to include; defaults to all
- supplier_ids — Two or more suppliers to compare
- spend_category — Restrict comparison to one spend category
- threshold — Overall score below which a supplier is flagged; defaults to 3.0, the lower bound of the Acceptable band (scores under it are the At risk band)
- supplier_ids — Suppliers to review; defaults to every active supplier
- period — Review period covered
- supplier_ids — Suppliers to audit; defaults to all

## Outputs

- One review per supplier, written as in the review route
- Summary dashboard of every review in the batch
- master-data-audit-report (markdown)
- supplier-alert-report (markdown)
- supplier-comparison (markdown)
- supplier-review (markdown)
- supplier-trend-report (markdown)
- {company.reports}/supplier_at_risk_{YYYY-MM-DD}.md
- {company.reports}/supplier_bulk_review_{YYYY-MM-DD}.md
- {company.reports}/supplier_comparison_{YYYY-MM-DD}.md
- {company.reports}/supplier_master_data_audit_{YYYY-MM-DD}.md
- {company.reports}/supplier_trend_{supplier-id}_{YYYY-MM-DD}.md
- {supplier.feedback}/review_{YYYY-MM-DD}.md


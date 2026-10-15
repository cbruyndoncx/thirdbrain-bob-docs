---
description: Aggregate deal data and prospect analyses across all clients into an executive-ready pipeline report with both Markdown and PDF output.
title: sales-pipeline-report
---

# sales-pipeline-report

Aggregate deal data and prospect analyses across all clients into an executive-ready pipeline report with both Markdown and PDF output.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Head of Sales

Generate sales pipeline reports with PDF output.

## How you ask

- “Generate a sales pipeline report with all active deals”
- “Create a pipeline health dashboard with score distribution”
- “Produce a forecast report across all client prospects”
- “Export the pipeline summary as a PDF report”

## Inputs

- lead-records — Canonical lead records, one folder per lead; select only notes whose frontmatter type is lead.
- deal-records — Deal records aggregated into the pipeline view.
- prospect-analyses — Prospect audit output, consumed as report input.
- brand-theme — Brand theme applied to the PDF deliverable.
- period — Reporting period; defaults to the current quarter
- include_clients — Clients to include; defaults to all non-demo clients
- client_id — Restrict the report to one client
- stage — Restrict to one pipeline stage (lead | lost | negotiation | proposal | qualified | won)

## Outputs

- pipeline-report (markdown)
- pipeline-report-pdf (pdf)
- {company.sales}/reports/pipeline_report_{YYYY-MM-DD}.md
- {company.sales}/reports/pipeline_report_{YYYY-MM-DD}.pdf


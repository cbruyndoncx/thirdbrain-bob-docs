---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: sales-pipeline-report — ThirdBrain BOB skill
  description: Aggregate deal data and prospect analyses across all clients into an executive-ready pipeline report with both Markdown and PDF output.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: sales-pipeline-report
catLabel: sales
area: sales
desc: Generate sales pipeline reports with PDF output.
summary: Aggregate deal data and prospect analyses across all clients into an executive-ready pipeline report with both Markdown and PDF output.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Sales]'
inputs:
- lead-records — Canonical lead records, one folder per lead; select only notes whose frontmatter type is lead.
- deal-records — Deal records aggregated into the pipeline view.
- prospect-analyses — Prospect audit output, consumed as report input.
- brand-theme — Brand theme applied to the PDF deliverable.
- period — Reporting period; defaults to the current quarter
- include_clients — Clients to include; defaults to all non-demo clients
- client_id — Restrict the report to one client
- stage — Restrict to one pipeline stage (lead | lost | negotiation | proposal | qualified | won)
outputs:
- pipeline-report (markdown)
- pipeline-report-pdf (pdf)
- '{company.sales}/reports/pipeline_report_{YYYY-MM-DD}.md'
- '{company.sales}/reports/pipeline_report_{YYYY-MM-DD}.pdf'
prompts:
- Generate a sales pipeline report with all active deals
- Create a pipeline health dashboard with score distribution
- Produce a forecast report across all client prospects
- Export the pipeline summary as a PDF report
---

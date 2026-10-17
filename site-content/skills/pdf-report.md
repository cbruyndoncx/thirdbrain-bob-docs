---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: pdf-report — ThirdBrain BOB skill
  description: Produce multi-page, client-ready PDF reports from structured JSON data. Visual components — gauges, bar charts, styled tables, colour-coded findings — are gener
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pdf-report
catLabel: documents
area: foundational
desc: Generate professional PDF reports from structured JSON data via ReportLab.
summary: Produce multi-page, client-ready PDF reports from structured JSON data. Visual components — gauges, bar charts, styled tables, colour-coded findings — are generic and theme-able. The calling skill (geo-audit, seo-audit, ad-hoc) owns all domain knowledge; this skill owns layout and rendering.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- report_json — JSON matching references/json_schema.md — meta object plus a sections array; pass '-' to read from stdin
- output_path — Explicit output PDF path — omitting it silently writes report.pdf into the current working directory
- theme — Company or per-client brand theme (logo, colours, typography); generic defaults apply when absent
- output_path — Not settable for the sample; the no-argument command always writes report-sample.pdf in the working directory
outputs:
- prefer a permanent directory)
- report-pdf (pdf)
- sample-pdf (pdf)
prompts:
- Generate a PDF report from this JSON data
- Create a client-ready PDF with score tables and gauges
- Export this structured data as a professional PDF document
- Build a PDF report with bar charts and findings cards
---

---
description: Produce multi-page, client-ready PDF reports from structured JSON data. Visual components — gauges, bar charts, styled tables, colour-coded findings — are generic and theme-able. The calling skill (geo-audit, seo-audit, ad-hoc) owns all domain knowledge; this skill owns layout and rendering.
title: pdf-report
---

# pdf-report

Produce multi-page, client-ready PDF reports from structured JSON data. Visual components — gauges, bar charts, styled tables, colour-coded findings — are generic and theme-able. The calling skill (geo-audit, seo-audit, ad-hoc) owns all domain knowledge; this skill owns layout and rendering.

- **Area:** Foundational
- **Category:** documents
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Generate professional PDF reports from structured JSON data via ReportLab.

## How you ask

- “Generate a PDF report from this JSON data”
- “Create a client-ready PDF with score tables and gauges”
- “Export this structured data as a professional PDF document”
- “Build a PDF report with bar charts and findings cards”

## Inputs

- report_json — JSON matching references/json_schema.md — meta object plus a sections array; pass '-' to read from stdin
- output_path — Explicit output PDF path — omitting it silently writes report.pdf into the current working directory
- theme — Company or per-client brand theme (logo, colours, typography); generic defaults apply when absent
- output_path — Not settable for the sample; the no-argument command always writes report-sample.pdf in the working directory

## Outputs

- prefer a permanent directory)
- report-pdf (pdf)
- sample-pdf (pdf)

## Seen in these workflows

- [The data is there.](../../workflows/foundational/pdf-report.md)


---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: PDF Report — The data is there
  description: Produce multi-page, client-ready PDF reports from structured JSON data. Visual components — gauges, bar charts, styled tables, colour-coded findings — are gener
  socialImage: https://img.youtube.com/vi/d88DBDMDfWI/maxresdefault.jpg
skillName: pdf-report
youtubeId: d88DBDMDfWI
published: ''
privacy: public
title: The data is there.
thumbnail: https://img.youtube.com/vi/d88DBDMDfWI/maxresdefault.jpg
subtitle: JSON → Professional PDF Report
inputs:
- label: Structured JSON data
  icon: 📋
- label: Report theme / meta config
  icon: 🎨
- label: Output path
  icon: 📁
outputs:
- label: Professional Report.pdf
  icon: 📕
- label: Score Gauges + Bar Charts
  icon: 📊
- label: Findings Cards + Action Plans
  icon: 📋
steps:
- Validating input JSON against schema
- Parsing meta block (title, subtitle, scores)
- Rendering 13 section types (gauges, charts, tables, prose)
- Assembling multi-page layout
- Generating final PDF via ReportLab
trigger: '"Generate a PDF report from this JSON data"'
timeSavings: ~2 hrs manual formatting → ~30 sec automated (240× faster)
compounding: Reusable across all skills — any structured data becomes a client-ready PDF
frequency: Per audit or deliverable · called by other skills
hook: 'The data is there.

  But it looks like a spreadsheet, not a deliverable.'
outcome: Professional PDF with scores, charts, findings cards, and action plans — from JSON.
benefits:
- 240× faster
- Client-ready formatting
- 13 section types — gauges, bars, tables, prose
cta: Generate a PDF report in 30 seconds
difficulty: beginner
primaryRoles: []
pricingTier: starter
category: documents
filterGroup: documents
area: foundational
---

Produce multi-page, client-ready PDF reports from structured JSON data. Visual components — gauges, bar charts, styled tables, colour-coded findings — are generic and theme-able. The calling skill (geo-audit, seo-audit, ad-hoc) owns all domain knowledge; this skill owns layout and rendering.

The data is there.

Professional PDF with scores, charts, findings cards, and action plans — from JSON.

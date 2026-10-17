---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: financial-reporting — ThirdBrain BOB skill
  description: 'Transform user-provided financial data into clear monthly reports: P&L summaries, cash position, AR/AP aging, margin by client or project, and month-over-month '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: financial-reporting
catLabel: finance
area: finance
desc: Generates monthly financial reports including P&L summaries, cash position, AR/AP aging, margin by client or project, and month-over-month comparisons.
summary: 'Transform user-provided financial data into clear monthly reports: P&L summaries, cash position, AR/AP aging, margin by client or project, and month-over-month comparisons. No ERP required — works from CSV or spreadsheet data.'
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- data — CSV or spreadsheet with revenue, expenses, cash, AR, and AP figures for the reporting month
- prior-month — Prior monthly snapshot for month-over-month comparison.
- data — Revenue and cost data by client, project, or service line (CSV or spreadsheet)
- period — Reporting period (e.g., "2026-03" or "Q1 2026"). Defaults to current month.
- cash-balance — Current cash balance
- burn-data — Monthly expense and revenue data to compute net burn (CSV or spreadsheet)
outputs:
- Monthly snapshot. Falls back to the scratch key when no vault structure is present.
- cash-runway (markdown)
- margin-analysis (markdown)
- '{scope.finance.reports}/cash_runway_{YYYY-MM}.md'
- '{scope.finance.reports}/margin_analysis_{YYYY-MM}.md'
- '{scope.finance.reports}/monthly_snapshot_{YYYY-MM}.md'
prompts:
- Show me the numbers
- How is cash
- Monthly financial report
---

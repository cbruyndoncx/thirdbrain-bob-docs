---
description: 'Transform user-provided financial data into clear monthly reports: P&L summaries, cash position, AR/AP aging, margin by client or project, and month-over-month comparisons. No ERP required — works from CSV or spreadsheet data.'
title: financial-reporting
---

# financial-reporting

Transform user-provided financial data into clear monthly reports: P&L summaries, cash position, AR/AP aging, margin by client or project, and month-over-month comparisons. No ERP required — works from CSV or spreadsheet data.

- **Area:** Finance
- **Category:** finance
- **Level:** beginner
- **Input:** data
- **Output:** spreadsheet
- **Setup:** none
- **Roles:** Finance Manager

Generates monthly financial reports including P&L summaries, cash position, AR/AP aging, margin by client or project, and month-over-month comparisons.

## How you ask

- “Show me the numbers”
- “How is cash”
- “Monthly financial report”

## Inputs

- data — CSV or spreadsheet with revenue, expenses, cash, AR, and AP figures for the reporting month
- prior-month — Prior monthly snapshot for month-over-month comparison.
- data — Revenue and cost data by client, project, or service line (CSV or spreadsheet)
- period — Reporting period (e.g., "2026-03" or "Q1 2026"). Defaults to current month.
- cash-balance — Current cash balance
- burn-data — Monthly expense and revenue data to compute net burn (CSV or spreadsheet)

## Outputs

- Monthly snapshot. Falls back to the scratch key when no vault structure is present.
- cash-runway (markdown)
- margin-analysis (markdown)
- {scope.finance.reports}/cash_runway_{YYYY-MM}.md
- {scope.finance.reports}/margin_analysis_{YYYY-MM}.md
- {scope.finance.reports}/monthly_snapshot_{YYYY-MM}.md


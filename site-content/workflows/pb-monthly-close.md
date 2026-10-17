---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Monthly Close — BOB Workflow
  description: Monthly Close
  socialImage: https://img.youtube.com/vi/d6ht2qsclXA/maxresdefault.jpg
skillName: pb-monthly-close
youtubeId: d6ht2qsclXA
published: '2026-08-01'
privacy: public
title: Monthly Close
thumbnail: https://img.youtube.com/vi/d6ht2qsclXA/maxresdefault.jpg
subtitle: Books reconciled, reports generated, and decisions made on what to adjust
inputs:
- label: Month being closed
  icon: 📋
- label: Bank statement(s) for the period
  icon: 📋
- label: Any known anomalies or one-off expenses
  icon: 📋
- label: Open questions from last month's close
  icon: 📋
outputs:
- label: Bank Ledger.csv
  icon: 📋
- label: P&L Report.pdf
  icon: 📊
- label: Aging Summaries.md
  icon: 📋
- label: MoM Comparison.md
  icon: 📋
- label: Decision Log.md
  icon: 📋
steps:
- label: financial-reporting → pull current month P&L, cash position, AR aging, AP aging
  actor: agent
- label: Reconcile bank statements against bookkeeping — flag discrepancies
  actor: human
- label: financial-reporting → generate month-over-month comparison, margin by client/project, cash runway
  actor: agent
- label: financial-decision-cadence → review red flags, highlight what needs attention, surface action triggers
  actor: agent
- label: 'Make decisions: chase overdue invoices, cut costs, adjust pricing, reallocate budget'
  actor: human
trigger: '"End of month — time to close the books and review financial position"'
timeSavings: 'Typical run: 2-4 hours per month'
compounding: Each run refines templates and context — 3 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'Month ended.

  The books close eventually. The decisions don''t.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: finance
---

Books reconciled, reports generated, and decisions made on what to adjust


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.

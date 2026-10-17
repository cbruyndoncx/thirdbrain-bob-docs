---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: demand-forecasting — ThirdBrain BOB skill
  description: Predict product demand from historical sales data, identify seasonal patterns, and project forward from the current order pipeline. Works from CSV or spreadshee
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: demand-forecasting
catLabel: operations
area: operations
desc: Predicts demand from historical sales data, seasonality patterns, and pipeline data.
summary: Predict product demand from historical sales data, identify seasonal patterns, and project forward from the current order pipeline. Works from CSV or spreadsheet exports — no BI tools, ERP access, or specialist software required.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- 'sales-data — CSV or spreadsheet with at minimum: date column, product/SKU column, quantity sold column'
- forecast-horizon — How far to forecast (e.g. 'next 4 weeks', 'next quarter'). Defaults to one period matching the input data granularity.
- method — Forecasting method. 'auto' selects based on data volume and variance. Defaults to auto. (simple-moving-average | weighted-moving-average | auto)
- sales-data — CSV or spreadsheet with date, product/SKU, and quantity columns. Minimum 24 months recommended.
- products — Comma-separated product names or SKUs to analyze. Omit to analyze all products in the file.
- pipeline-data — CSV or spreadsheet with open orders, quotes, or enquiries — including expected close date and quantity.
- conversion-rate — Historical quote-to-order conversion rate as a percentage (e.g. '65%'). If omitted, the skill will ask.
- lead-time-weeks — Production or procurement lead time in weeks. Used to flag urgent gaps.
outputs:
- forecast-table (markdown)
- pipeline-forecast (markdown)
- prefer a permanent directory)
- seasonal-index-table (markdown)
prompts:
- Forecast demand for next quarter from this sales CSV
- Which of our products have seasonal peaks and when are they?
- Based on our current order book, what do we need to make in the next 8 weeks?
- Set inventory targets for each SKU based on last year's data
- Flag any open quotes that we can't fulfill if they all convert this month
---

---
description: Build sales forecasts grounded in pipeline data and historical conversion rates, not feelings. Categorize deals into commit/upside/best-case, calculate weighted pipeline, run sanity checks, and produce actionable forecast reports. Separately, compare prior forecasts to actual outcomes to diagnose accuracy patterns and bias.
title: sales-forecast
---

# sales-forecast

Build sales forecasts grounded in pipeline data and historical conversion rates, not feelings. Categorize deals into commit/upside/best-case, calculate weighted pipeline, run sanity checks, and produce actionable forecast reports. Separately, compare prior forecasts to actual outcomes to diagnose accuracy patterns and bias.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Head of Sales

Builds sales forecasts from vault deal and lead records with commit, upside, and best-case pipeline categorization.

## How you ask

- “Forecast revenue”
- “Quota attainment”
- “Commit number”

## Inputs

- lead-records — Lead records — the prospects being worked.
- deal-records — Deal records the forecast is built from.
- profile — Company or client profile — entity and relationship context.
- pipeline_data — Active deals from the client deals folders (`client.deals`) and the lead profiles under the company leads folder (`{company.leads}`, one `{lead.profile}` per lead)
- forecast_period — Month or quarter being forecast (e.g., 2026-Q2, 2026-04)
- revenue_target — Quota or revenue goal for the period — ask if not provided
- prior_forecasts — Previous forecast reports from the company sales folder (`company.sales`, subfolder `reports/`), filename `sales_forecast_*.md`
- actuals — Closed-won deal data and revenue actuals for the same periods

## Outputs

- accuracy_report (markdown)
- forecast_report (markdown)
- {company.sales}/reports/forecast_accuracy_{YYYY-MM-DD}.md
- {company.sales}/reports/sales_forecast_{YYYY-MM-DD}.md


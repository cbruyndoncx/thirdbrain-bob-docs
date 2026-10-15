---
description: Transform raw business data into clear reports with analysis, visualizations, and recommendations.
title: business-reporting
---

# business-reporting

Transform raw business data into clear reports with analysis, visualizations, and recommendations.

- **Area:** Strategy
- **Category:** business
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Finance Manager

Generates business reports including financial cohort analyses, campaign ROI calculations, quarterly business reviews (QBRs), and revenue forecasts.

## How you ask

- “Create a quarterly business review report for Q1”
- “Run a cohort analysis on our customer retention data”
- “Calculate the ROI of our latest marketing campaign”
- “Generate a revenue forecast for the next 12 months”

## Inputs

- company-profile — Company profile — entity and reporting context for the cohort output.
- transaction-data — Transaction data with customer ID, purchase date, and amount, used to assign cohorts and compute per-cohort retention and revenue.
- request — The cohort question to answer, including cohort period (monthly/weekly) and any focus cohort.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- campaign-data — Campaign spend, impressions, clicks, conversions, and revenue data used to calculate ROI, ROAS, and the channel breakdown.
- profile — Company or client profile, matching `scope` — entity and reporting context for the campaign.
- request — The ROI question to answer, including the campaign name, channel(s), and attribution model to use.
- profile — Company or client profile, matching `scope`, and prior reporting context for the executive narrative.
- quarter-data — The quarter's revenue, KPI, and highlight/challenge data used to build the scorecard and narrative.
- okr-progress — Current-quarter OKR progress read back from `okr-frameworks`, included in the scorecard's OKR Progress section when available.
- request — The QBR scope to cover — which quarter, and any emphasis (revenue, risk, OKRs).
- company-profile — Company profile — entity and reporting context for the forecast narrative.
- historical-revenue-data — Historical monthly or quarterly revenue data used to fit the forecast method and build scenario projections.
- request — The forecast horizon and any known drivers or constraints to factor into the scenarios.

## Outputs

- Cohort retention and revenue/LTV tables with methodology, key findings, and recommendations.
- Executive QBR — summary, KPI scorecard, revenue analysis, wins, risks, OKR progress, and next-quarter priorities.
- ROI/ROAS analysis with channel breakdown, attribution notes, and scale/optimize/cut recommendations.
- Scenario revenue projections with method, assumptions, key drivers, and risks.
- {company.reports}/qbr_{YYYY}_q{X}.md (company scope) or {client.deliverables}/qbr_{YYYY}_q{X}.md (client scope)
- {scope.finance.analysis}/cohort_analysis_{YYYY-MM}.md
- {scope.finance.analysis}/revenue_forecast_{YYYY-MM}.md
- {scope.marketing}/campaign_roi_{name}.md


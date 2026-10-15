---
description: Comprehensive GA4 reference covering property setup, events, custom dimensions, audiences, reporting, BigQuery integration, and implementation methods.
title: ga4-analytics
---

# ga4-analytics

Comprehensive GA4 reference covering property setup, events, custom dimensions, audiences, reporting, BigQuery integration, and implementation methods.

- **Area:** Marketing
- **Category:** marketing analytics
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** Head of Marketing

Covers Google Analytics 4 property setup, events, audiences, reporting, BigQuery, gtag.js, GTM, and DebugView.

## How you ask

- “Set up GA4 property with recommended events”
- “Configure custom dimensions for user segmentation in GA4”
- “Implement GA4 event tracking with gtag.js”
- “Set up BigQuery integration for our GA4 data”

## Inputs

- client-profile — Client profile — property owner context.
- profile — Company profile (`company.profile`) — Business model, product type
- tracking-plan — Latest tracking plan from analytics-tracking (`analytics/tracking-plan-{YYYY-MM-DD}.md` under `company.marketing` or `client.marketing`), read so GA4 event and parameter names match the plan
- url — Website URL whose GA4 implementation is being set up or checked, when the task concerns a specific site
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- GA4 deliverable, one file per type: `setup` (property and data streams), `events` (event implementation), `reporting` (custom dimensions and audiences)


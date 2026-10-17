---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ga4-analytics — ThirdBrain BOB skill
  description: Comprehensive GA4 reference covering property setup, events, custom dimensions, audiences, reporting, BigQuery integration, and implementation methods.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ga4-analytics
catLabel: marketing-analytics
area: marketing
desc: Covers Google Analytics 4 property setup, events, audiences, reporting, BigQuery, gtag.js, GTM, and DebugView.
summary: Comprehensive GA4 reference covering property setup, events, custom dimensions, audiences, reporting, BigQuery integration, and implementation methods.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[Head of Marketing]'
inputs:
- client-profile — Client profile — property owner context.
- profile — Company profile (`company.profile`) — Business model, product type
- tracking-plan — Latest tracking plan from analytics-tracking (`analytics/tracking-plan-{YYYY-MM-DD}.md` under `company.marketing` or `client.marketing`), read so GA4 event and parameter names match the plan
- url — Website URL whose GA4 implementation is being set up or checked, when the task concerns a specific site
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- 'GA4 deliverable, one file per type: `setup` (property and data streams), `events` (event implementation), `reporting` (custom dimensions and audiences)'
prompts:
- Set up GA4 property with recommended events
- Configure custom dimensions for user segmentation in GA4
- Implement GA4 event tracking with gtag.js
- Set up BigQuery integration for our GA4 data
---

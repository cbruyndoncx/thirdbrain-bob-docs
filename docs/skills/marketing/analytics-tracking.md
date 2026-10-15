---
description: Set up analytics tracking that provides actionable insights for marketing and product decisions. Covers tracking plans, event naming, GA4/GTM implementation, and validation workflows.
title: analytics-tracking
---

# analytics-tracking

Set up analytics tracking that provides actionable insights for marketing and product decisions. Covers tracking plans, event naming, GA4/GTM implementation, and validation workflows.

- **Area:** Marketing
- **Category:** marketing analytics
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** Head of Marketing

Creates tracking plans, configures GA4 events and conversions, implements GTM data layers, designs UTM parameter strategies, and validates event firing with debug tools.

## How you ask

- “Create a tracking plan for our new product launch”
- “Set up GA4 event tracking for our signup flow”
- “Design a UTM parameter strategy for our campaigns”
- “Implement a GTM data layer for our e-commerce site”

## Inputs

- marketing_context — Business goals and KPIs that decide which conversions are worth an event at all.
- request — The decisions the data has to inform and the surfaces in scope for the event map.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- current-state — Analytics tools already in place and what they already capture, so the plan extends the existing naming rather than forking a second convention.
- request — Which events still need instrumenting and any constraint on how they can be deployed.
- tracking-plan — Event map from the `tracking-plan` route, read back so the implemented event and property names match the plan instead of being renamed at deploy time.
- platform — Which deployment path the instructions target. The choice decides whether the output is gtag calls written into the page or a data-layer contract plus container configuration. (ga4 | gtm | both)
- tech-context — Stack, CMS, and privacy or consent constraints that bound how tags can be injected and when they may fire.
- request — Which events or conversions are distrusted and the symptom that prompted the check.
- tracking-plan — Event map from the `tracking-plan` route, read back to give the validation a declared expected state to test observed firing against.
- debug-evidence — Observed firing captured from DebugView, GTM Preview, or a tag inspector, with the date range it covers. Absent, the route reports the missing validation as a blocker rather than passing the tracking.
- marketing_context — Campaign and channel mix the convention has to cover without inventing channels that are not run.
- request — The attribution problem to fix — inconsistent values, unattributable traffic, or a new campaign set needing a convention up front.
- channels — The paid, email, social, and referral channels the convention must assign source and medium values for.

## Outputs

- Conversion list, event and property table with triggers, the naming convention, and the assumptions and exclusions behind each entry.
- Per-event pass or fail against the validation checklist, the duplicates and missing properties found, the conversion-marking check, and any validation that could not be run.
- Per-event setup instructions, data-layer or gtag payloads, conversion marking steps, consent handling, and the deployment sequence.
- The agreed source, medium, campaign, content, and term value sets, the usage rules and casing standard, and worked example URLs per channel.
- {scope.marketing}/analytics/tracking-implementation-{YYYY-MM-DD}.md
- {scope.marketing}/analytics/tracking-plan-{YYYY-MM-DD}.md
- {scope.marketing}/analytics/tracking-validation-{YYYY-MM-DD}.md


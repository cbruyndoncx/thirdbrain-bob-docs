---
description: Full-funnel CRO covering pages, forms, popups, signup flows, onboarding, and paywall/upgrade screens. Each area has a detailed reference file — read the relevant one for deep-dive checklists, code examples, and experiment ideas.
title: cro
---

# cro

Full-funnel CRO covering pages, forms, popups, signup flows, onboarding, and paywall/upgrade screens. Each area has a detailed reference file — read the relevant one for deep-dive checklists, code examples, and experiment ideas.

- **Area:** Marketing
- **Category:** marketing funnel
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** Head of Marketing, Product Manager

General conversion rate optimization for landing pages, forms, popups, signup flows, and exit intent.

## How you ask

- “Optimize conversions on our signup page”
- “Analyze the form abandonment on our checkout flow”
- “Review this URL and suggest CRO improvements”
- “Design a popup strategy for exit-intent visitors”
- “Improve our onboarding flow to reduce drop-off”

## Inputs

- url — Live page to fetch and score. This route cannot run without it — there is no vault context to fall back on.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The single page and conversion problem the audit is scoped to.
- url — Live address of the page, when one exists to fetch and score alongside the vault context.
- profile — Business model and target market used to pick the page-type conversion benchmark the score is read against.
- icp — Ideal customer profile the headline, proof hierarchy, and objection handling are judged against.
- marketing-context — Positioning and differentiation the rewritten value proposition has to stay consistent with.
- request — The form or signup flow under audit and where abandonment is observed.
- url — Live address of the form or first signup step, when one exists to fetch.
- icp — Ideal customer profile used to decide which fields are genuinely qualifying and which can be deferred.
- marketing-context — Trust and risk-reversal claims already made elsewhere, reused to remove uncertainty at the point of capture.
- request — The popup or overlay under audit, its purpose (email capture, lead magnet, discount, exit save), and the problem seen — low conversion, high close rate, or complaints.
- url — Live page where the popup shows, when one exists to fetch.
- marketing-context — Offer, lead magnets, and audience the popup copy and targeting have to match.
- request — The onboarding flow under audit and the drop-off already observed, with the activation event if one is defined.
- profile — Product type and business model used to pick a realistic activation event for this kind of product.
- icp — Ideal customer profile used to judge which first-run step a new user will actually complete unaided.
- request — The paywall or upgrade screen under audit and the upgrade problem — low intent, wrong moment, or wrong package.
- profile — Business model and current packaging that the upgrade moment has to sell against.
- icp — Ideal customer profile used to judge when in the user's journey the upgrade ask is credible.
- marketing-context — Positioning and guarantee claims the upgrade screen reuses to reduce perceived risk.

## Outputs

- A/B tests derived from the page audit, each with hypothesis, variant, and the metric that decides it.
- Field removals, label and micro-copy fixes, and validation changes that can ship without a test cycle.
- Field-by-field friction analysis, error-handling findings, and the reduced-field target with its rationale.
- Fixes that can ship without a test cycle, ranked by expected conversion effect over effort.
- Onboarding experiments from `references/experiments-onboarding.md`, each with hypothesis and success metric.
- Paywall experiments from `references/experiments-paywall.md`, each with hypothesis and success metric.
- Popup design (type, trigger, targeting, frequency, copy), compliance and accessibility findings, severity-ranked.
- Popup experiments from `references/popup.md` → Experiment Ideas, each with hypothesis and success metric.
- Section-by-section page analysis with severity-ranked recommendations and before/after copy examples.
- Step map with the drop-off at each step, the named activation event, and the single largest drop to fix first.
- Value-clarity, risk, timing, and packaging findings for the upgrade moment, severity-ranked.
- Weighted 7-Point score with per-section scores against the detected page-type benchmark, weakest areas first.
- {scope.marketing}/cro/cro-audit-{YYYY-MM-DD}.md
- {scope.marketing}/cro/cro-quick-wins-{page-or-flow}.md
- {scope.marketing}/cro/cro-test-plan-{page-or-flow}.md

## Seen in these workflows

- [Visitors come.](../../workflows/marketing/cro.md)


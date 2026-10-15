---
description: Expert guidance for SaaS pricing and monetization strategy. Design pricing that captures value, drives growth, and aligns with customer willingness to pay.
title: pricing-strategy
---

# pricing-strategy

Expert guidance for SaaS pricing and monetization strategy. Design pricing that captures value, drives growth, and aligns with customer willingness to pay.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing strategy |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Head of Sales, Product Manager] |

Selects monetization models, analyzes competitive pricing, designs tier structures, recommends value metrics, and conducts Van Westendorp analysis.

## How you ask

- “Design a three-tier pricing structure for our SaaS product”
- “Analyze competitive pricing in our market”
- “Should we offer a free trial or freemium model?”
- “Run a Van Westendorp analysis for our pricing”

## Inputs

- profile — Scope-resolved profile: `company.profile` for own-business work; `client.profile` for client work. Caller resolves the path from the active client-id (`self` → company; otherwise → client).
- offerings — Scope-resolved offerings: `company.offerings` for own-business work; `client.offerings` for client work.
- icp — Scope-resolved ICP: `company.icp` for own-business work; `client.icp` for client work.
- marketing-context — Positioning, competitors, and differentiation used to judge which revenue model the market will accept.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — The monetization question to answer, including any models already ruled in or out.
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
- profile — Scope-resolved profile: `company.profile` for own-business work; `client.profile` for client work.
- offerings — Current products, packaging, and prices the new structure has to replace or extend.
- icp — Ideal customer profile used to set tier boundaries against real buying units.
- marketing-context — Positioning and differentiation that the tier names and feature gates have to stay consistent with.
- region-context — Currency, purchasing power, and regulatory pricing rules for the target market; produced by `regional-context`.
- pricing-analysis — Research output from the `research` route, read back so tier price points rest on measured willingness to pay rather than assumption.
- won-deal-evidence — Won-deal notes, call transcripts or win-loss analyses in the customers' own words, used to classify each offer component as Leader, Filler, Add-on or Killer. Absent, the classification is labelled a hypothesis.
- request — The packaging problem to solve — number of tiers, which value metric is under consideration, known constraints.
- icp — Ideal customer profile defining who the willingness-to-pay figures are meant to describe.
- marketing-context — Named competitors and differentiation claims that set the comparison set for competitor price analysis.
- region-context — Currency and purchasing-power baseline so price points from different markets are comparable.
- survey-data — Raw Van Westendorp or MaxDiff responses exported from the survey tool. Absent, the route designs the instrument instead of analysing results.
- request — The evidence question — which method, which segment, and what decision the numbers will feed.
- offerings — The pricing in force today — the baseline the change is measured against.
- icp — Ideal customer profile used to judge which existing cohorts absorb the change and which churn.
- region-context — Regulatory notice periods and currency rules that constrain how a live price may be changed.
- pricing-structure — Target structure from the `pricing-structure` route, read back when the change is a move to a designed structure rather than a flat increase.
- request — The change under consideration and its trigger — margin pressure, repositioning, or a competitor move.

## Outputs

- Leader check, change rationale, grandfathering rule, customer comms plan, rollout sequence, success metrics, and rollback trigger.
- Model comparison, fit assessment against segment and GTM motion, and the validation plan for the recommended model.
- Offer component classification (Leader, Filler, Add-on, Killer), value metric, tier definitions, feature differentiation, and price points with the assumptions behind each.
- Research findings, competitor price set, and acceptable-price range, each labelled with its evidence quality.


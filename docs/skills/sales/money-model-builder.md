---
description: Design and sequence a complete offer ladder — attraction offer → flagship → upsell → order bump → downsell → continuity — and model the cash it collects in the first 30 days, all grounded in the business's existing vault offer, ICP, and positioning context.
title: money-model-builder
---

# money-model-builder

Design and sequence a complete offer ladder — attraction offer → flagship → upsell → order bump → downsell → continuity — and model the cash it collects in the first 30 days, all grounded in the business's existing vault offer, ICP, and positioning context.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Head of Marketing, Head of Sales

Designs a full offer ladder and 30-day cash model from your existing vault offer, ICP, and positioning — attraction offer, flagship, upsell, order bump, downsell, and…

## How you ask

- “Build my money model”
- “Design my offer ladder”
- “What should my upsell be”

## Inputs

- product-record — Product records — the offers in the ladder.
- icp — Ideal customer profile — who the output targets.
- marketing_context — Positioning and messaging context.
- offerings — Offerings catalogue — what is being sold.
- source (Ladder Design) — Optional offer/product name or focus area; defaults to the vault's canonical offer if omitted
- source (30-Day Cash Model) — The offer ladder (from ladder-design) or a described ladder, plus assumed front-end volume
- source (Ladder Audit) — The existing ladder to audit (pasted, or a path to a prior money-model note)

## Outputs

- cash-model (markdown)
- ladder-audit (markdown)
- money-model (markdown)
- {company.sales}/money-models/cash-model-{offer}-{date}.md
- {company.sales}/money-models/ladder-audit-{offer}-{date}.md
- {company.sales}/money-models/money-model-{offer}-{date}.md


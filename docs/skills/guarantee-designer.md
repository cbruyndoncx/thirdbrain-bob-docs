---
description: Remove the buyer's risk. Design guarantees that convert hesitation into commitment.
title: guarantee-designer
---

# guarantee-designer

Remove the buyer's risk. Design guarantees that convert hesitation into commitment.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Sales] |

Designs risk-reversal guarantees for proposals and offers.

## How you ask

- “Design a guarantee for our 90-day AI transformation service”
- “Our main objection is 'we tried AI before and it didn't stick' — what guarantee fixes that?”
- “Audit our current guarantee: [paste existing guarantee text]”
- “We want premium positioning with no refunds — how do we make that work?”
- “Give me 3 guarantee options for a $25,000 B2B service”

## Inputs

- profile — Company or client profile — entity and relationship context.
- service-context — Service promise, delivery controls, buyer fear, price, proof, and company profile context.
- risk-context — Outcome variability, customer obligations, operational exposure, exclusions, and claim history.
- existing-guarantee — Existing guarantee copy plus conversion, claim, and buyer-objection evidence.

## Outputs

- guarantee (markdown)
- guarantee-audit (markdown)
- guarantee-options (markdown)
- optimized-guarantee (markdown)
- {scope.sales}/guarantee-audit-{date}.md
- {scope.sales}/guarantee-options-{service}-{date}.md
- {scope.sales}/guarantee-{service}-{date}.md


---
description: Design and optimize referral and affiliate programs that turn customers into growth engines. Covers program types, incentive structures, viral loops, and optimization strategies.
title: referral-program
---

# referral-program

Design and optimize referral and affiliate programs that turn customers into growth engines. Covers program types, incentive structures, viral loops, and optimization strategies.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing funnel |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Head of Sales] |

Designs tiered reward structures, calculates commission rates, creates referral tracking workflows, and drafts partner program terms.

## How you ask

- “Design a tiered referral program for our SaaS product”
- “Calculate commission rates for our affiliate program”
- “Create a refer-a-friend campaign with tracking workflow”
- “Draft partner program terms and reward structures”

## Inputs

- request — Program type (referral, affiliate, or both), business model, current referral rate, and any supplied program constraints
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- affiliate-program-design (markdown)
- company-referral-program (markdown)
- referral-program-brief (markdown)
- referral-program-design (markdown)
- referral-program-review (markdown)
- {client.marketing}/referral/affiliate-program-design.md
- {client.marketing}/referral/referral-program-brief.md
- {client.marketing}/referral/referral-program-design.md
- {client.marketing}/referral/referral-program-review.md
- {scope.marketing}/referral/referral-program-{YYYY-MM-DD}.md


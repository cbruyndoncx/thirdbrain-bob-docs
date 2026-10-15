---
description: Discover, pitch, and partner with micro-influencers and newsletter creators to reach targeted audiences and acquire customers through trusted recommendations.
title: influencer-outreach
---

# influencer-outreach

Discover, pitch, and partner with micro-influencers and newsletter creators to reach targeted audiences and acquire customers through trusted recommendations.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** Head of Marketing

Plans influencer and newsletter sponsorship campaigns for customer acquisition.

## How you ask

- “Find micro-influencers in the productivity niche for our tool”
- “Create a pitch template for newsletter sponsorship outreach”
- “Plan an influencer marketing campaign with a $5K budget”
- “Build a list of creator partnership opportunities for our brand”

## Inputs

- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- icp — loaded from your vault context
- marketing-context — loaded from your vault context

## Outputs

- influencer-outreach (markdown)
- {scope.marketing}/influencer-outreach/influencer-outreach-{YYYY-MM-DD}.md


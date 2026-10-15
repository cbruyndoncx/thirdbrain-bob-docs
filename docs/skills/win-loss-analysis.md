---
description: Structured analysis of closed deals to extract the real reasons behind wins and losses, identify patterns across deal outcomes, and generate actionable recommendations for sales execution, competitive positioning, and product strategy.
title: win-loss-analysis
---

# win-loss-analysis

Structured analysis of closed deals to extract the real reasons behind wins and losses, identify patterns across deal outcomes, and generate actionable recommendations for sales execution, competitive positioning, and product strategy.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Head of Sales] |

Analyze why deals were won or lost, extract competitive intelligence from deal outcomes, and find patterns across closed deals.

## How you ask

- “Why did we lose that deal”
- “Win-loss review”
- “Analyze our closed deals”

## Inputs

- profile — Company or client profile — entity and relationship context.
- deal_data — Deal details: company name, outcome, value, timeline, stakeholders, competitor, rep notes, and any buyer feedback or interview transcripts
- client_id — Client ID if deal record exists in vault (the client's deals folder, `client.deals`)
- deal_data — Multiple deal records: CRM export, spreadsheet, or structured list of closed deals with outcomes, values, loss reasons, competitors, and timelines
- period — Time period for analysis (e.g., 'Q1 2026', 'last 6 months')

## Outputs

- Complete deal analysis with profile, timeline, buyer journey reconstruction, real reason, key moments, and recommendations
- Pattern analysis with segment breakdowns, loss reason distribution, competitive win/loss, win themes, and prioritized recommendations
- {company.sales}/win-loss/batch_analysis_{YYYY-MM-DD}.md
- {company.sales}/win-loss/{deal-slug}_analysis_{YYYY-MM-DD}.md


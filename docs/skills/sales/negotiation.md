---
description: Prepare deal negotiation strategies and coach through multi-round B2B negotiations -- from BATNA analysis and concession planning through stakeholder handling and close.
title: negotiation
---

# negotiation

Prepare deal negotiation strategies and coach through multi-round B2B negotiations -- from BATNA analysis and concession planning through stakeholder handling and close.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Head of Sales

Prepare negotiation strategy, plan concessions, structure deals, and coach through multi-round negotiations.

## How you ask

- “They want a discount”
- “Help me negotiate this deal”
- “Procurement is pushing back”

## Inputs

- profile — Company or client profile — entity and relationship context.
- deal_context — Deal summary: product/service, proposed price, contract terms, and what the buyer is pushing back on
- client_id — Client identifier (kebab-case) for vault routing
- deal_slug — Short deal identifier for filenames (kebab-case)
- stakeholders — Key people involved: champion, procurement, decision-maker, legal
- round_update — What happened in the latest round: what they said, what was offered, what was rejected
- existing_prep — Prior negotiation prep document from the prep route.

## Outputs

- Full negotiation strategy document with BATNA, concession tiers, stakeholder plays, and closing approach
- Running negotiation tracker with round history, agreed items, open items, and next-move recommendation
- {client.sales}/negotiations/{deal-slug}_negotiation_prep_{YYYY-MM-DD}.md
- {client.sales}/negotiations/{deal-slug}_negotiation_tracker_{YYYY-MM-DD}.md


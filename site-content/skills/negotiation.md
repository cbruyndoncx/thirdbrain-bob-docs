---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: negotiation — ThirdBrain BOB skill
  description: Prepare deal negotiation strategies and coach through multi-round B2B negotiations -- from BATNA analysis and concession planning through stakeholder handling a
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: negotiation
catLabel: sales
area: sales
desc: Prepare negotiation strategy, plan concessions, structure deals, and coach through multi-round negotiations.
summary: Prepare deal negotiation strategies and coach through multi-round B2B negotiations -- from BATNA analysis and concession planning through stakeholder handling and close.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Sales]'
inputs:
- profile — Company or client profile — entity and relationship context.
- 'deal_context — Deal summary: product/service, proposed price, contract terms, and what the buyer is pushing back on'
- client_id — Client identifier (kebab-case) for vault routing
- deal_slug — Short deal identifier for filenames (kebab-case)
- 'stakeholders — Key people involved: champion, procurement, decision-maker, legal'
- 'round_update — What happened in the latest round: what they said, what was offered, what was rejected'
- existing_prep — Prior negotiation prep document from the prep route.
outputs:
- Full negotiation strategy document with BATNA, concession tiers, stakeholder plays, and closing approach
- Running negotiation tracker with round history, agreed items, open items, and next-move recommendation
- '{client.sales}/negotiations/{deal-slug}_negotiation_prep_{YYYY-MM-DD}.md'
- '{client.sales}/negotiations/{deal-slug}_negotiation_tracker_{YYYY-MM-DD}.md'
prompts:
- They want a discount
- Help me negotiate this deal
- Procurement is pushing back
---

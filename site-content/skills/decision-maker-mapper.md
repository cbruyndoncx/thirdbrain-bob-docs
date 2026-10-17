---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: decision-maker-mapper — ThirdBrain BOB skill
  description: Map the buying committee, build an org chart, find personalization anchors, and design a multi-threading engagement strategy for a prospect company.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: decision-maker-mapper
catLabel: sales
area: sales
desc: Map buying committee and decision makers for a prospect company.
summary: Map the buying committee, build an org chart, find personalization anchors, and design a multi-threading engagement strategy for a prospect company.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- company — Target organization to map
- deal_context — What is being sold, to focus the map on relevant roles
- icp — ICP — defines the buyer persona profile to map against.
- calling_skill — Skill invoking this one, which sets the output shape
outputs:
- decision-maker-map (markdown)
- '{client.sales}/decision_maker_map.md'
prompts:
- Map the decision makers at Acme Corp
- Identify the buying committee for this enterprise deal
- Who decides on technology purchases at this company?
- Build an engagement strategy for the target org chart
---

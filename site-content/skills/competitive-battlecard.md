---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: competitive-battlecard — ThirdBrain BOB skill
  description: 'Generate structured competitive battlecards — concise, scannable quick-reference documents that sales teams use mid-conversation to position against a specific '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: competitive-battlecard
catLabel: sales
area: sales
desc: Generates structured competitive battlecards for sales teams.
summary: Generate structured competitive battlecards — concise, scannable quick-reference documents that sales teams use mid-conversation to position against a specific competitor.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- competitor — Competitor name or URL
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- icp — ICP to frame why we win vs this competitor.
- marketing-context — Positioning context for differentiation framing.
- offerings — Offerings for feature/price comparison.
- profile — Company or client profile for identity and credibility.
- competitors — List of competitor names or URLs
- icp — ICP to frame why we win vs these competitors.
outputs:
- battlecard (markdown)
- client-output-artifact (markdown)
- '{client.sales}/battlecards/{competitor-slug}.md'
- '{company.sales}/battlecards/overview_{date}.md'
- '{company.sales}/battlecards/{competitor-slug}.md'
prompts:
- Create a battlecard for competing against HubSpot
- 'Build a competitive cheat sheet: us vs Salesforce'
- Battlecard comparing us against HubSpot, Pipedrive, and Freshsales
- Update the Salesforce battlecard with their new pricing
---

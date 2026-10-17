---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: icp-discovery — ThirdBrain BOB skill
  description: 'Build structured Ideal Customer Profiles through a guided discovery interview. Supports B2B, B2C, and owner-operator buyer models. Produces a comprehensive ICP '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: icp-discovery
catLabel: marketing-strategy
area: marketing
desc: Builds Ideal Customer Profiles through guided discovery interviews and persona templates.
summary: Build structured Ideal Customer Profiles through a guided discovery interview. Supports B2B, B2C, and owner-operator buyer models. Produces a comprehensive ICP document with demographics/firmographics, buyer psychology, pains, scoring signals, and buying journey.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Marketing, Head of Sales]'
inputs:
- profile — Business identity and overview — own-business or client based on scope.
- offerings — Products and services that the ICP buys.
- marketing-context — Positioning and differentiation context for the ICP.
- company-deep-research-report — Optional prior research report — adds depth to ICP build.
- request — What to produce
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
- icp — Existing ICP document to base the buying-committee map on.
- profile — Business identity — own-business or client based on scope.
- offerings — Offerings the buying committee is evaluating.
- request — Which account or ICP to map the buying committee for
outputs:
- buying_committee_map (markdown)
- icp (markdown)
- icp_index (markdown)
- icp_scoring_card (markdown)
- '{scope.icp}'
- '{scope.profile-root}/buying_committee_map.md'
- '{scope.profile-root}/icp_index.md'
- '{scope.profile-root}/icp_scoring_card.md'
prompts:
- Help me define our ideal customer profile
- Run a guided discovery interview to build our buyer persona
- Identify the key demographics and pain points of our target audience
- Create a persona template from our customer research
- Map the buying committee for our ICP
- Build champion and blocker personas for our deals
- Who's involved in our deals and how do we multi-thread?
---

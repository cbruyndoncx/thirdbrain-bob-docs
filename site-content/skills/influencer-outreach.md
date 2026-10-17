---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: influencer-outreach — ThirdBrain BOB skill
  description: Discover, pitch, and partner with micro-influencers and newsletter creators to reach targeted audiences and acquire customers through trusted recommendations.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: influencer-outreach
catLabel: marketing-content
area: marketing
desc: Plans influencer and newsletter sponsorship campaigns for customer acquisition.
summary: Discover, pitch, and partner with micro-influencers and newsletter creators to reach targeted audiences and acquire customers through trusted recommendations.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[Head of Marketing]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- icp — loaded from your vault context
- marketing-context — loaded from your vault context
outputs:
- influencer-outreach (markdown)
- '{scope.marketing}/influencer-outreach/influencer-outreach-{YYYY-MM-DD}.md'
prompts:
- Find micro-influencers in the productivity niche for our tool
- Create a pitch template for newsletter sponsorship outreach
- Plan an influencer marketing campaign with a $5K budget
- Build a list of creator partnership opportunities for our brand
---

---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: launch-strategy — ThirdBrain BOB skill
  description: You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and conve
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: launch-strategy
catLabel: marketing-strategy
area: marketing
desc: Create launch timelines, draft announcement copy, plan Product Hunt campaigns, and design waitlist strategies.
summary: You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into users.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- profile — Business model and product overview.
- offerings — Products being launched.
- icp — Target audience for the launch.
- marketing-context — Positioning, channels, and differentiation.
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
outputs:
- launch-assets-brief (markdown)
- launch-calendar (markdown)
- launch-checklist (markdown)
- launch-plan (markdown)
- launch-review (markdown)
- prefer a permanent directory)
- temporary-launch-strategy (markdown)
- '{scope.marketing}/launches/launch-calendar.md'
- '{scope.marketing}/launches/{product}/launch-assets-brief.md'
- '{scope.marketing}/launches/{product}/launch-checklist.md'
- '{scope.marketing}/launches/{product}/launch-plan.md'
- '{scope.marketing}/launches/{product}/launch-review.md'
prompts:
- Create a launch timeline for our new product release
- Plan a Product Hunt launch campaign
- Design a waitlist strategy for our beta launch
- Draft announcement copy for our feature release
---

---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: paywall-upgrade-cro — ThirdBrain BOB skill
  description: Design paywalls that match the upgrade moment, explain value clearly, and preserve trust.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: paywall-upgrade-cro
catLabel: marketing-funnel
area: marketing
desc: Deep-dive into free-to-paid conversion — designs paywall copy, structures upgrade flows, creates feature gates, and optimizes trial expiration screens.
summary: Design paywalls that match the upgrade moment, explain value clearly, and preserve trust.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- paywall-upgrade-cro (markdown)
- '{scope.marketing}/experiments/paywall-upgrade-cro-{YYYY-MM-DD}.md'
prompts:
- Design persuasive upgrade copy for our paywall screen
- Optimize our free-to-paid conversion flow
- Create feature gate copy that drives upgrades
- Write trial expiration modal copy that converts
---

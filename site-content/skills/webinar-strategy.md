---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: webinar-strategy — ThirdBrain BOB skill
  description: Plan, promote, and execute webinars that acquire customers by embedding product value into educational content delivered to borrowed audiences.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: webinar-strategy
catLabel: marketing-content
area: marketing
desc: Plans and executes webinar-based customer acquisition strategies.
summary: Plan, promote, and execute webinars that acquire customers by embedding product value into educational content delivered to borrowed audiences.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- topic — Webinar topic or buyer pain point to address
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- icp — loaded from your vault context
- marketing-context — loaded from your vault context
outputs:
- webinar-strategy (markdown)
- '{scope.marketing}/webinars/webinar-strategy-{YYYY-MM-DD}.md'
prompts:
- Plan a webinar series for our product launch
- Create a guest speaker outreach template for our webinar
- Design a webinar promotion campaign with email sequences
- Build a webinar outline for our AI automation workshop
---

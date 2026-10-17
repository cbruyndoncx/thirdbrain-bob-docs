---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: email-sequence — ThirdBrain BOB skill
  description: Create email sequences that nurture relationships, drive action, and move people toward conversion. Covers sequence types, timing, copy guidelines, and automati
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: email-sequence
catLabel: marketing-funnel
area: marketing
desc: Creates lifecycle and nurture email campaigns — welcome sequences, onboarding drips, re-engagement flows, and segmentation logic.
summary: Create email sequences that nurture relationships, drive action, and move people toward conversion. Covers sequence types, timing, copy guidelines, and automation strategies.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- profile — Company or client profile — entity and relationship context.
- request — What to produce
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
outputs:
- email-copy (markdown)
- email-sequence (markdown)
- email-sequence-brief (markdown)
- email-templates (markdown)
- '{scope.marketing.email}/email-sequence-brief-{name}.md'
- '{scope.marketing.email}/email-sequence-{name}.md'
- '{scope.marketing.email}/email-templates-{category}.md'
- '{scope.marketing.email}/email-{sequence}-{number}.md'
prompts:
- Create a welcome email sequence for new subscribers
- Design a 5-email nurture drip campaign for trial users
- Write a re-engagement email sequence for churned customers
- Build an onboarding email sequence with optimized timing
---

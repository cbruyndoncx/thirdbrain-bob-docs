---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: growth-embedded — ThirdBrain BOB skill
  description: Use this skill when growth should be designed into the product deliberately, not bolted on after launch.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: growth-embedded
catLabel: product-management
area: strategy
desc: Designs activation loops, viral growth mechanics, product-led growth features, user acquisition loops, onboarding sequences, and referral tracking inside the product.
summary: Use this skill when growth should be designed into the product deliberately, not bolted on after launch.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- growth-embedded (markdown)
- '{scope.knowledge-base.product}/growth-embedded-{YYYY-MM-DD}.md'
prompts:
- Design a viral growth loop for our product
- Build activation mechanics for our onboarding flow
- Create a referral tracking system inside our product
- Design product-led growth features for user acquisition
---

---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: referral-program — ThirdBrain BOB skill
  description: Design and optimize referral and affiliate programs that turn customers into growth engines. Covers program types, incentive structures, viral loops, and optimi
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: referral-program
catLabel: marketing-funnel
area: marketing
desc: Designs tiered reward structures, calculates commission rates, creates referral tracking workflows, and drafts partner program terms.
summary: Design and optimize referral and affiliate programs that turn customers into growth engines. Covers program types, incentive structures, viral loops, and optimization strategies.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Head of Sales]'
inputs:
- request — Program type (referral, affiliate, or both), business model, current referral rate, and any supplied program constraints
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- affiliate-program-design (markdown)
- company-referral-program (markdown)
- referral-program-brief (markdown)
- referral-program-design (markdown)
- referral-program-review (markdown)
- '{client.marketing}/referral/affiliate-program-design.md'
- '{client.marketing}/referral/referral-program-brief.md'
- '{client.marketing}/referral/referral-program-design.md'
- '{client.marketing}/referral/referral-program-review.md'
- '{scope.marketing}/referral/referral-program-{YYYY-MM-DD}.md'
prompts:
- Design a tiered referral program for our SaaS product
- Calculate commission rates for our affiliate program
- Create a refer-a-friend campaign with tracking workflow
- Draft partner program terms and reward structures
---

---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: linkedin-outreach — ThirdBrain BOB skill
  description: Expert B2B LinkedIn outreach and social selling. LinkedIn is the only platform where you can reach a CEO, see their career history, read their recent posts, and
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: linkedin-outreach
catLabel: sales
area: sales
desc: Write LinkedIn outreach messages, design LinkedIn outreach campaigns, or plan social selling strategy.
summary: Expert B2B LinkedIn outreach and social selling. LinkedIn is the only platform where you can reach a CEO, see their career history, read their recent posts, and send them a message in one place. Most LinkedIn outreach is terrible, which is both the problem and the opportunity. Treat LinkedIn as a relationship-building channel, not a spam cannon.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- lead-records — Lead profile notes — the prospects being worked, one folder per lead.
- offerings — Offerings catalogue — what is being sold.
- profile — Company or client profile — entity and relationship context.
- prospect_context — Who the prospect is, their LinkedIn activity level, what you sell, pain you solve, proof points
- 'message_type — connection-request, dm-sequence, inmail, comment-strategy, or video-message (default: dm-sequence)'
- campaign_goal — Campaign objective (book meetings, build pipeline, generate referrals, enter new vertical)
- sales_navigator — Whether Sales Navigator is available (changes targeting and InMail options)
outputs:
- Campaign plan with targeting, sequences, content calendar, and benchmarks
- LinkedIn outreach messages ready for manual sending
- '{company.sales.outbound}/{campaign-slug}_linkedin_campaign_plan_{YYYY-MM-DD}.md'
- '{company.sales.outbound}/{campaign-slug}_linkedin_outreach_{YYYY-MM-DD}.md'
prompts:
- LinkedIn message
- Connection request
- InMail template
---

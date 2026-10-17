---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: local-outreach — ThirdBrain BOB skill
  description: Build local relationships that generate customers through community presence, in-person networking, and hyper-local digital engagement.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: local-outreach
catLabel: marketing-content
area: marketing
desc: Creates local relationship-building strategies for customer acquisition.
summary: Build local relationships that generate customers through community presence, in-person networking, and hyper-local digital engagement.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing]'
inputs:
- icp — Ideal customer profile — who the output targets.
- profile — Company or client profile — entity and relationship context.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- local-outreach (markdown)
- local-outreach-company (markdown)
- '{client.marketing}/local-outreach/local-outreach-{YYYY-MM-DD}.md'
- '{company.marketing}/local-outreach/local-outreach-{YYYY-MM-DD}.md'
prompts:
- Create a local networking strategy for our consulting firm
- Draft a chamber of commerce introduction script
- Plan community outreach for our new co-working space
- Generate engagement templates for local Facebook groups
---

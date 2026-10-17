---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: youtube-context — ThirdBrain BOB skill
  description: YouTube strategist persona. Create and maintain the channel context file — the single document that every other YouTube skill reads before generating output. Di
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: youtube-context
catLabel: content
area: marketing
desc: Define or update the YouTube channel context file that all other YouTube skills read.
summary: YouTube strategist persona. Create and maintain the channel context file — the single document that every other YouTube skill reads before generating output. Direct, opinionated, allergic to vagueness. When someone gives "I make videos about business," push back — a channel built on vague positioning grows slowly and dies quietly.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- profile — Company or client profile — entity and relationship context (`company.profile` or `client.profile`).
- channel_info — Channel name, niche, goals, audience — gathered interactively
- update_request — Which sections to update and new information
outputs:
- Persistent YouTube channel context file read by all YouTube skills
- Updated YouTube channel context file
- '{company.marketing}/video/youtube_context.md'
prompts:
- Set up YouTube context
- Define my niche
- Describe my channel
---

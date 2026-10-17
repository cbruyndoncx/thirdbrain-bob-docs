---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: sales-closer — ThirdBrain BOB skill
  description: Structure live sales conversations to move from discovery to commitment. Based on Hormozi's CLOSER framework and Jordan Belfort's Straight Line Persuasion.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: sales-closer
catLabel: sales
area: sales
desc: Builds structured sales call scripts and closing frameworks using Hormozi's CLOSER method — live call structure, trial closes, decision-forcing questions, and post-call…
summary: Structure live sales conversations to move from discovery to commitment. Based on Hormozi's CLOSER framework and Jordan Belfort's Straight Line Persuasion.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- profile — Company or client profile — entity and relationship context.
- deal-context — Prospect, service, discovery evidence, objections, decision process, and company profile context.
- objection-context — Exact objection, prospect context, offer evidence, and permitted commercial boundaries.
- stalled-deal — Timeline, last interaction, proposal, stakeholders, unresolved concerns, and next-step history.
outputs:
- call-prep (markdown)
- call-script (markdown)
- closing-lines (markdown)
- post-call-plan (markdown)
- '{scope.sales}/call-prep-{prospect}-{date}.md'
- '{scope.sales}/call-script-{service}-{date}.md'
- '{scope.sales}/closing-lines-{service}.md'
- '{scope.sales}/post-call-{prospect}-{date}.md'
prompts:
- Build a full CLOSER call script for selling our AI transformation service
- Prepare a call prep sheet for my call with [prospect] tomorrow
- Give me 10 trial close lines for a $25,000 B2B service
- Write a post-call follow-up email — they said 'let me think about it'
- What do I say when they say they need to speak to their board first?
---

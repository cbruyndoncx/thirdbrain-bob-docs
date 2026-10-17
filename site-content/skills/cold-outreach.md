---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: cold-outreach — ThirdBrain BOB skill
  description: 'Build cold DM sequences on LinkedIn, WhatsApp, and Instagram that get replies — not just opens. Volume-based, personalized at scale, with multi-touch follow-up '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: cold-outreach
catLabel: marketing-funnel
area: marketing
desc: Builds cold DM sequences for LinkedIn, WhatsApp, and Instagram — personalized openers, multi-touch follow-up cadences, volume activity targets, and trigger-event timing.
summary: Build cold DM sequences on LinkedIn, WhatsApp, and Instagram that get replies — not just opens. Volume-based, personalized at scale, with multi-touch follow-up cadences.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- icp — Ideal customer profile — who the output targets.
- profile — Company or client profile — entity and relationship context.
- outreach-context — ICP, company profile, segment, offer, proof, and channel constraints.
- outreach-context — ICP, segment, offer, proof, consent context, and chosen messaging channel.
- prospect-context — Named prospect, relevance evidence, offer, desired next step, and profile context.
- activity-targets — Channels, daily volumes, reply stages, owners, and tracking period.
- email-context — Segment, offer, proof, and required cold-email outcome to hand off.
outputs:
- Handoff to `cold-email` naming the segment, offer and proof to pass it; this skill writes no email copy.
- cold-dm-sequence (markdown)
- cold-email (markdown)
- outreach-tracker (markdown)
- '{scope.sales}/cold-dm-seq-{segment}-{date}.md'
- '{scope.sales}/cold-email-{prospect}-{date}.md'
- '{scope.sales}/outreach-tracker-{date}.md'
prompts:
- Build a WhatsApp DM sequence for CFOs at UAE manufacturing companies
- Build a LinkedIn outreach sequence for mid-market HR Directors
- 'Write a single LinkedIn DM for this prospect: [paste company/role info]'
- What's my daily outreach target if I want 3 calls/week?
---

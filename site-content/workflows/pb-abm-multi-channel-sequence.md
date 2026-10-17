---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: ABM Multi Channel Sequence
  description: ABM Multi-Channel Sequence — qualified conversations with target accounts
  socialImage: https://img.youtube.com/vi/hP6H_TTaiCU/maxresdefault.jpg
skillName: pb-abm-multi-channel-sequence
youtubeId: hP6H_TTaiCU
published: '2026-06-29'
privacy: public
title: ABM Multi-Channel Sequence — qualified conversations with target accounts
thumbnail: https://img.youtube.com/vi/hP6H_TTaiCU/maxresdefault.jpg
subtitle: Pipeline of qualified conversations with decision-makers at target accounts across 3 tiers
inputs:
- label: ICP definition (from `icp-discovery` or existing profile)
  icon: 🎯
- label: Target region(s)
  icon: 🎯
- label: Sector focus — which industries to prioritize
  icon: 🏭
- label: Outreach tool in use — Instantly / Apollo / manual
  icon: 📋
- label: LinkedIn account for outreach (company page or personal profile)
  icon: 🏢
- label: Number of accounts per tier to activate
  icon: 🔢
outputs:
- label: Account list with tier assignments
  icon: 📋
- label: T1 account research notes + buying committee maps
  icon: 🎙️
- label: Sequence copy per tier (email + LinkedIn)
  icon: 📧
- label: Active campaign tracker
  icon: 📋
steps:
- label: '`linkedin-searches` → build target account list matching ICP; aim for T1: 10, T2: 30, T3: 80'
  actor: agent
- label: Tier and prioritize accounts — score each on fit (ICP match), intent signals (LinkedIn activity, job posts, news), and relationship warmth; assign T1/T2/T3
  actor: human
- label: Personalization hooks — for T1 note 2–3 specific hooks per account (recent post, milestone, team challenge, sector trend); for T2 note 1 hook per segment; for T3 use ICP-level pain framing only
  actor: human
- label: '`outbound-sequence` → design the per-tier touch plan (channels, day spacing, breakpoints) using the specs below'
  actor: agent
- label: '`cold-email` → write the email copy variants for each tier — intro, value, ask, breakup — keyed to the touch plan'
  actor: agent
- label: '`linkedin-outreach` → write the LinkedIn copy variants — connect requests, content engagement, DMs — keyed to the touch plan'
  actor: agent
- label: Stage and launch — load sequences into outreach tool; confirm personalization fields populated for T1 and T2 before sending
  actor: human
trigger: '"Decision to run an account-based outreach campaign targeting a defined set of accounts"'
timeSavings: 'Typical run: 3-5 hours initial setup; sequences run 4-6 weeks'
compounding: Each run refines templates and context — 4 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'Fifty target accounts.

  One generic sequence for all of them.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Builds a tiered account list, designs the per-tier touch plan, and writes email + LinkedIn copy per tier.

More at brn.cx

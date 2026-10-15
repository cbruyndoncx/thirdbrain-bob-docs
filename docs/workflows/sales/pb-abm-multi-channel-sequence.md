---
title: ABM Multi-Channel Sequence — qualified conversations with target accounts
---

# ABM Multi-Channel Sequence — qualified conversations with target accounts

*Pipeline of qualified conversations with decision-makers at target accounts across 3 tiers*

<div class="video-wrap"><iframe width="100%" height="420" src="https://www.youtube.com/embed/hP6H_TTaiCU?rel=0" title="ABM Multi-Channel Sequence — qualified conversations with target accounts" frameborder="0" allowfullscreen loading="lazy"></iframe></div>

> Fifty target accounts.
> One generic sequence for all of them.

- **Area:** Sales & Clients
- **Time savings:** Typical run: 3-5 hours initial setup; sequences run 4-6 weeks
- **Try it:** "Decision to run an account-based outreach campaign targeting a defined set of accounts"
- **Compounding:** Each run refines templates and context — 4 automated steps improve with accumulated data
- **Frequency:** Per opportunity
- **Published:** 2026-06-29

## Inputs

- 🎯 ICP definition (from `icp-discovery` or existing profile)
- 🎯 Target region(s)
- 🏭 Sector focus — which industries to prioritize
- 📋 Outreach tool in use — Instantly / Apollo / manual
- 🏢 LinkedIn account for outreach (company page or personal profile)
- 🔢 Number of accounts per tier to activate

## What BOB does

1. `linkedin-searches` → build target account list matching ICP; aim for T1: 10, T2: 30, T3: 80
2. Tier and prioritize accounts — score each on fit (ICP match), intent signals (LinkedIn activity, job posts, news), and relationship warmth; assign T1/T2/T3
3. Personalization hooks — for T1 note 2–3 specific hooks per account (recent post, milestone, team challenge, sector trend); for T2 note 1 hook per segment; for T3 use ICP-level pain framing only
4. `outbound-sequence` → design the per-tier touch plan (channels, day spacing, breakpoints) using the specs below
5. `cold-email` → write the email copy variants for each tier — intro, value, ask, breakup — keyed to the touch plan
6. `linkedin-outreach` → write the LinkedIn copy variants — connect requests, content engagement, DMs — keyed to the touch plan
7. Stage and launch — load sequences into outreach tool; confirm personalization fields populated for T1 and T2 before sending

## Outputs

- 📋 Account list with tier assignments
- 🎙️ T1 account research notes + buying committee maps
- 📧 Sequence copy per tier (email + LinkedIn)
- 📋 Active campaign tracker


---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: outbound-sequence — ThirdBrain BOB skill
  description: Expert outbound sales strategist who designs and optimizes multi-channel sequences across SMB, mid-market, and enterprise sales motions. Sequencing is where mos
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: outbound-sequence
catLabel: sales
area: sales
desc: Design multi-channel outbound sequences orchestrating cold email, phone, LinkedIn, and direct mail into a cohesive cadence.
summary: Expert outbound sales strategist who designs and optimizes multi-channel sequences across SMB, mid-market, and enterprise sales motions. Sequencing is where most outbound fails — not because the emails or calls are bad, but because the timing, channel mix, and persistence are wrong.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- target_persona — Who the sequence targets — title, company size, seniority level, industry
- deal_size — Expected deal size range — determines sequence length and channel investment
- available_channels — Channels the team has access to — email, phone, LinkedIn Sales Nav, direct mail
- 'meeting_target — Monthly meeting target for capacity math (default: 10)'
- icp — ICP for targeting and messaging.
- offerings — Offerings for sequence value proposition.
- profile — Company or client profile for identity framing.
outputs:
- Complete multi-channel outbound sequence with timing, channel mix, capacity math, branching logic, and exit criteria
- '{company.sales.outbound}/{campaign-slug}_outbound_sequence_{YYYY-MM-DD}.md'
prompts:
- Build me a sequence
- Create a cadence
- Multi-channel outreach plan
---

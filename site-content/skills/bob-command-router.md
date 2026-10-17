---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: bob-command-router — ThirdBrain BOB skill
  description: Route natural language requests to one of six BOB commands, collect the required inputs, and hand off to the appropriate playbook or skill for execution.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: bob-command-router
catLabel: utilities
area: foundational
desc: Route natural language to BOB playbook chains.
summary: Route natural language requests to one of six BOB commands, collect the required inputs, and hand off to the appropriate playbook or skill for execution.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- business-description — What the business does
- challenge — Biggest current challenge
- offer — Current offer and target customer
- sales-process — Current sales process and monthly leads
- website-url — Website URL
- channels — Social channels, marketing spend, target audience
- process — A core process to document
- current-state — Current state, desired state, top 3 constraints
- product — loaded from your vault context
- client-id — The at-risk client's client-id (kebab-case, validated per Constraints)
- 'what-changed — Signals that changed: late payment, missed meetings, NPS drop, escalation, executive turnover'
- renewal-date — Contract renewal date, or 'rolling'
- stakes — Revenue at risk, strategic importance, reference value
outputs:
- annual_plan (markdown)
- annual_plan_pdf (pdf)
- business_baseline (drawio)
- growth_plan (markdown)
- growth_plan_pdf (pdf)
- marketing_plan (markdown)
- playbook (markdown)
- save_plan (markdown)
- save_plan_pdf (pdf)
- '{client.business-baseline}/{client-id}-business-baseline.drawio'
- '{client.deliverables}/fix-my-marketing.md'
- '{client.deliverables}/fix-my-retention.md'
- '{client.deliverables}/fix-my-retention.pdf'
- '{client.deliverables}/grow-my-revenue.md'
- '{client.deliverables}/grow-my-revenue.pdf'
- '{client.deliverables}/plan-my-next-12-months.md'
- '{client.deliverables}/plan-my-next-12-months.pdf'
- '{company.playbooks}/{playbook-name}.md'
prompts:
- Analyze my business — I run a cleaning company and I'm stuck at 500K revenue
- Help me grow my revenue, I need more B2B leads
- My marketing isn't working, can you fix it?
- I want to build a playbook for our client onboarding process
- Help me plan my next 12 months — I want to double my team size
---

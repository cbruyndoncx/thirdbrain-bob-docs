---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: cac-payback-playbook — ThirdBrain BOB skill
  description: Calculates CAC payback period for funded startups AND bootstrapped SMBs. Startup route covers investor-grade benchmarks, cohort presentations, and Q&A prep. SMB
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: cac-payback-playbook
catLabel: product-management
area: strategy
desc: Calculates CAC payback period for funded startups AND bootstrapped SMBs.
summary: Calculates CAC payback period for funded startups AND bootstrapped SMBs. Startup route covers investor-grade benchmarks, cohort presentations, and Q&A prep. SMB route covers channel-level ROI triage, cash flow constraints, and marketing spend decisions. Use when user mentions 'CAC payback,' 'customer acquisition cost,' 'unit economics,' 'marketing ROI,' 'is my marketing working,' 'payback period,' 'channel ROI.' This is the CAC payback methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Finance Manager]'
inputs:
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- company_data — Company stage, sector, ACV, revenue model, spend/revenue data
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- company_profile — Stage, sector, ACV range
- cac_data — Existing CAC payback numbers and unit economics
- business_data — Industry, revenue range, marketing channels, monthly spend, new customers, pricing, gross margin
- channel_data — Per-channel spend, customer counts, and revenue data
outputs:
- cac-benchmarks (markdown)
- cac-payback-analysis (markdown)
- channel-triage (markdown)
- investor-prep (markdown)
- marketing-payback-diagnostic (markdown)
- '{scope.knowledge-base.product}/cac-investor-prep-{YYYY-MM-DD}.md'
- '{scope.knowledge-base.product}/cac-payback-analysis-{YYYY-MM-DD}.md'
- '{scope.knowledge-base.product}/cac-payback-benchmarks-{YYYY-MM-DD}.md'
- '{scope.knowledge-base.product}/channel-roi-triage-{YYYY-MM-DD}.md'
- '{scope.knowledge-base.product}/marketing-payback-diagnostic-{YYYY-MM-DD}.md'
prompts:
- Calculate our CAC payback period for our Series A deck
- How does our CAC payback compare to SaaS benchmarks?
- Prepare me for investor questions about unit economics
- Where do we sit on the NDR/CAC matrix?
- Is my marketing spend paying back fast enough?
- Which of my marketing channels should I cut?
- How fast can I grow without running out of cash?
- I spend $5K/month on marketing — is it working?
---

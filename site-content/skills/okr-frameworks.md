---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: okr-frameworks — ThirdBrain BOB skill
  description: 'Writes effective OKRs, aligns team goals, and creates measurement frameworks for quarterly progress tracking. Use when user mentions ''OKR,'' ''objectives and key '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: okr-frameworks
catLabel: product-management
area: strategy
desc: Writes effective OKRs, aligns team goals, and creates measurement frameworks for quarterly progress tracking.
summary: Writes effective OKRs, aligns team goals, and creates measurement frameworks for quarterly progress tracking. Use when user mentions 'OKR,' 'objectives and key results,' 'quarterly goals,' 'goal setting,' 'team alignment.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- kpi_registry — Canonical KPI ids and thresholds. Key results bind to an existing id where one fits, rather than defining a parallel metric that drifts from the weekly KPI loop.
- request — The planning scope — team, quarter, and the company or product priorities the OKRs must support.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- kpi_registry — Canonical KPI ids and thresholds, used to confirm each key result is bound to a real metric rather than an ad-hoc one.
- existing-okrs — The OKR set under review, produced by a prior `okr-structure` run, checked objective by objective against the quality checklist.
- request — Which OKR set to review and what triggered the check — quarter close, KR cleanup, or a pre-lock review.
outputs:
- Fresh OKR brief — 2-3 objectives, each with 3-5 measurable key results, why-it-matters, owner, and reporting cadence.
- Revised OKR set with quality-check findings applied and any remaining instrumentation or dependency gaps flagged.
- '{scope.knowledge-base.product}/okr-frameworks-{YYYY-MM-DD}.md'
prompts:
- Write OKRs for our product team this quarter
- Align our team goals with the company objectives
- Create a measurement framework for tracking our Q2 goals
- Review and refine these OKRs for clarity and ambition
---

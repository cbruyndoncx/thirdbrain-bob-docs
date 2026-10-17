---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: growth-scaling-playbook — ThirdBrain BOB skill
  description: Use this skill as the default entrypoint for generic business-growth questions. It does not own channel tactics, product-led growth mechanics, or proprietary co
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: growth-scaling-playbook
catLabel: product-management
area: strategy
desc: Diagnoses revenue plateaus with a growth-stage framework, the binding constraint, and a 90-day focus.
summary: Use this skill as the default entrypoint for generic business-growth questions. It does not own channel tactics, product-led growth mechanics, or proprietary coaching frameworks. It diagnoses stage, identifies the binding constraint, chooses the right downstream skills, and returns a focused 90-day plan.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- profile — Company or client profile — identity, revenue pattern, and stage evidence the diagnosis is built on.
- icp — ICP used to judge whether acquisition, conversion, or delivery is the real constraint for this customer.
- offerings — Offerings catalogue used to check whether the constraint is offer-side before recommending downstream skills.
- marketing-context — Positioning, narrative, and competitive frame used to rule positioning in or out as the binding constraint.
- region-context — Regional business environment for the target market, included in the diagnosis and 90-day plan when the profile has `regions[]` set; produced by `regional-context`.
- request — The growth question to diagnose, including the pain point in the user's own words.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Whatever company or client profile exists — read opportunistically; the route runs even when it is thin or missing.
- icp — ICP, if it exists, used to sanity-check the likely stage rather than as a hard input.
- region-context — Regional business environment, if available, noted as an assumption rather than fetched fresh for this quick read; produced by `regional-context`.
- request — The growth question to orient on and why a quick read rather than a full diagnosis is wanted.
outputs:
- Growth stage, the single binding constraint, the specialist-skill handoff, and a three-priority 90-day action plan with owners, metrics, and stage-transition criteria.
- Likely growth stage with stated assumptions, the probable binding constraint, the evidence still missing, and the next one or two actions — not a full 90-day plan.
- '{scope.knowledge-base.product}/growth-scaling-playbook-{YYYY-MM-DD}.md'
prompts:
- Why has our growth stalled at $2M ARR?
- What's the binding constraint holding back our scaling?
- Diagnose our revenue plateau and recommend focus areas
- What should we focus on in the next 90 days to grow?
---

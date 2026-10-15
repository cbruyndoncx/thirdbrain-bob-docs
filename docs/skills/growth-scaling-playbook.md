---
description: Use this skill as the default entrypoint for generic business-growth questions. It does not own channel tactics, product-led growth mechanics, or proprietary coaching frameworks. It diagnoses stage, identifies the binding constraint, chooses the right downstream skills, and returns a focused 90-day plan.
title: growth-scaling-playbook
---

# growth-scaling-playbook

Use this skill as the default entrypoint for generic business-growth questions. It does not own channel tactics, product-led growth mechanics, or proprietary coaching frameworks. It diagnoses stage, identifies the binding constraint, chooses the right downstream skills, and returns a focused 90-day plan.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Product Manager] |

Diagnoses revenue plateaus with a growth-stage framework, the binding constraint, and a 90-day focus.

## How you ask

- “Why has our growth stalled at $2M ARR?”
- “What's the binding constraint holding back our scaling?”
- “Diagnose our revenue plateau and recommend focus areas”
- “What should we focus on in the next 90 days to grow?”

## Inputs

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

## Outputs

- Growth stage, the single binding constraint, the specialist-skill handoff, and a three-priority 90-day action plan with owners, metrics, and stage-transition criteria.
- Likely growth stage with stated assumptions, the probable binding constraint, the evidence still missing, and the next one or two actions — not a full 90-day plan.
- {scope.knowledge-base.product}/growth-scaling-playbook-{YYYY-MM-DD}.md

## Seen in these workflows

- [Growth stalled.](../workflows/growth-scaling-playbook.md)


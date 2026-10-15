---
description: Use this skill to design the operating system around feedback, not just to list survey ideas.
title: user-feedback-system
---

# user-feedback-system

Use this skill to design the operating system around feedback, not just to list survey ideas.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Product Manager] |

Builds feedback collection systems, measures product-market fit, and structures user research cadences.

## How you ask

- “Build a feedback collection system for our product”
- “Set up an NPS survey and measurement cadence”
- “Measure product-market fit with a PMF survey”
- “Structure our user research interviews for this quarter”

## Inputs

- request — The PMF question — designing the survey, or interpreting a current "very disappointed" score against the 40% threshold.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The retention, satisfaction, or friction question — NPS cadence design, interview program setup, or theme synthesis from responses already collected.
- request — The feature-request prioritization problem, assuming synthesis and theme rules already exist — which requests to score and how to close the loop.

## Outputs

- Feature-request backlog scored by RICE, the roadmap decisions it drives, and the close-the-loop message to users.
- NPS and interview operating plan — cadence, current score and promoter/passive/detractor split, and themes surfaced from interviews.
- PMF survey design or score interpretation — current "very disappointed" percentage, trend, and the iterate-or-hold call.
- {scope.knowledge-base.product}/user-feedback-system-{YYYY-MM-DD}.md


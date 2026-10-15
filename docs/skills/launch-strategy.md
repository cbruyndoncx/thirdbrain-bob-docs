---
description: You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into users.
title: launch-strategy
---

# launch-strategy

You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into users.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing strategy |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Product Manager] |

Create launch timelines, draft announcement copy, plan Product Hunt campaigns, and design waitlist strategies.

## How you ask

- “Create a launch timeline for our new product release”
- “Plan a Product Hunt launch campaign”
- “Design a waitlist strategy for our beta launch”
- “Draft announcement copy for our feature release”

## Inputs

- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- profile — Business model and product overview.
- offerings — Products being launched.
- icp — Target audience for the launch.
- marketing-context — Positioning, channels, and differentiation.
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set

## Outputs

- launch-assets-brief (markdown)
- launch-calendar (markdown)
- launch-checklist (markdown)
- launch-plan (markdown)
- launch-review (markdown)
- prefer a permanent directory)
- temporary-launch-strategy (markdown)
- {scope.marketing}/launches/launch-calendar.md
- {scope.marketing}/launches/{product}/launch-assets-brief.md
- {scope.marketing}/launches/{product}/launch-checklist.md
- {scope.marketing}/launches/{product}/launch-plan.md
- {scope.marketing}/launches/{product}/launch-review.md


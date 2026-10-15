---
description: Use this skill when the team needs a usable positioning artifact, not just abstract messaging advice.
title: positioning-craft
---

# positioning-craft

Use this skill when the team needs a usable positioning artifact, not just abstract messaging advice.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Head of Marketing, Product Manager] |

Crafts product positioning, defines target customers, chooses market categories, and articulates differentiated value.

## How you ask

- “Craft our product positioning against the competition”
- “Define our target customer and market category”
- “Articulate our differentiated value proposition”
- “Help me position our new feature in the market”

## Inputs

- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- product — What is being positioned
- competitive_alternatives — What customers would use instead
- target_segment — Segment to position for; defaults to the vault ICP
- icp — ICP — target customer the positioning is for.
- profile — Company profile — identity and proof points.
- marketing-context — Prior positioning, narrative, and competitive frame.
- tone-of-voice — Tone of voice — keeps the new positioning on-brand.
- offerings — Offerings catalogue — what is being positioned.
- current_positioning — Positioning statement as it stands today
- what_is_not_landing — Which part is failing, and the evidence for it
- messages — Message variants to test
- audience — Audience to test against; defaults to the vault ICP

## Outputs

- positioning-brief (markdown)
- {scope.profile-root}/positioning-{slug}.md


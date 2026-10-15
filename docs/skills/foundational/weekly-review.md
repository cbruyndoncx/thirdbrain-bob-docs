---
description: A structured 15-minute CEO operating rhythm that replaces the vague anxiety of "am I working on the right things?" with clarity. Six sections, conversational flow, concrete output.
title: weekly-review
---

# weekly-review

A structured 15-minute CEO operating rhythm that replaces the vague anxiety of "am I working on the right things?" with clarity. Six sections, conversational flow, concrete output.

- **Area:** Foundational
- **Category:** productivity
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder

Runs a structured 15-minute weekly CEO check-in covering scorecard metrics, wins, losses and lessons, priority progress, next week's focus, and energy levels.

## How you ask

- “Weekly review”
- “End of week check-in”
- “How did this week go”

## Inputs

- profile — Company or client profile — entity and relationship context.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- review_config — Metrics and priorities from the `setup` route that the scorecard section is checked against.
- context — Founder's responses to the six review sections
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
- business_context — Company overview, quarterly priorities, key metrics, current challenges

## Outputs

- Business context, quarterly priorities and the key metrics each weekly review scores against.
- weekly_review (markdown)
- {company.profile-root}/weekly_review_config.md
- {vault.weekly-notes}/weekly_review_{YYYY-MM-DD}.md


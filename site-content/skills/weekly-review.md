---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: weekly-review — ThirdBrain BOB skill
  description: A structured 15-minute CEO operating rhythm that replaces the vague anxiety of "am I working on the right things?" with clarity. Six sections, conversational fl
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: weekly-review
catLabel: productivity
area: foundational
desc: Runs a structured 15-minute weekly CEO check-in covering scorecard metrics, wins, losses and lessons, priority progress, next week's focus, and energy levels.
summary: A structured 15-minute CEO operating rhythm that replaces the vague anxiety of "am I working on the right things?" with clarity. Six sections, conversational flow, concrete output.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder]'
inputs:
- profile — Company or client profile — entity and relationship context.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- review_config — Metrics and priorities from the `setup` route that the scorecard section is checked against.
- context — Founder's responses to the six review sections
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
- business_context — Company overview, quarterly priorities, key metrics, current challenges
outputs:
- Business context, quarterly priorities and the key metrics each weekly review scores against.
- weekly_review (markdown)
- '{company.profile-root}/weekly_review_config.md'
- '{vault.weekly-notes}/weekly_review_{YYYY-MM-DD}.md'
prompts:
- Weekly review
- End of week check-in
- How did this week go
---

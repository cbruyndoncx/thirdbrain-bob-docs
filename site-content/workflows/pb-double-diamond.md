---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Double Diamond — BOB Workflow
  description: Double Diamond
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-double-diamond
youtubeId: ''
published: ''
privacy: unlisted
title: Double Diamond
thumbnail: ''
subtitle: One committed problem statement and one committed solution concept, each chosen against recorded alternatives, handed to Concept-to-Launch for delivery
inputs:
- label: Problem area or opportunity statement (symptom-level, solution-free)
  icon: 📋
- label: Customer access or existing research corpus
  icon: 🔍
- label: Available resources (budget, team, timeline)
  icon: 💰
- label: Constraints that any solution must respect
  icon: 📦
outputs:
- label: Discovery Signal.md
  icon: 📋
- label: JTBD Map.md
  icon: 🗺️
- label: Problem Statement.md (with rejected framings)
  icon: 📋
- label: Solution Concepts.md (three or more, with the board's debate)
  icon: 📋
- label: Concept Ranking.md
  icon: 📋
- label: Ship Decision.md
  icon: 📋
- label: Everything produced by [[Concept-to-Launch]]
  icon: 📅
steps:
- label: continuous-discovery → gather problem-space signal from customers; capture symptoms and unmet needs without proposing solutions
  actor: agent
- label: jtbd-building → map customer jobs, push/pull/anxiety/habit forces, and current workarounds across the gathered signal
  actor: agent
- label: Commit ONE problem statement. Record every framing considered and why each rejected one lost
  actor: human
- label: ask-boardroom → convene the board to generate and debate at least three genuinely distinct solution concepts for the committed problem
  actor: agent
- label: prioritization-craft → score the competing concepts against a single framework and produce a ranked list
  actor: agent
- label: Commit ONE solution concept. Record the runners-up and the reason each lost
  actor: human
- label: ship-decisions → classify the committed concept's reversibility and set explicit go/no-go criteria
  actor: agent
- label: '[[Concept-to-Launch]] → execute build, positioning, launch, and measurement for the committed concept'
  actor: agent
trigger: '"A problem or opportunity needs deliberate exploration before a solution is committed — the team is at risk of building the first idea that surfaced"'
timeSavings: 'Typical run: 1-3 weeks for the two diamonds, before delivery begins'
compounding: Each run refines templates and context — 6 automated steps improve with accumulated data
frequency: Per trigger event
hook: You picked the solution before you agreed on the problem.
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---



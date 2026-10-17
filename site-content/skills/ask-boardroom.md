---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ask-boardroom — ThirdBrain BOB skill
  description: Simulate a board of strategic advisors to debate your toughest business decisions.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ask-boardroom
catLabel: business
area: strategy
desc: Simulate a board of advisors for strategic decisions, or run 1:1 strategic sparring sessions.
summary: Simulate a board of strategic advisors to debate your toughest business decisions.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder]'
inputs:
- request — What to produce
- scope — `company`, or a client-id resolving to the client's folder (`client.root`) — a string with one reserved value, not a closed set
- decision — The decision or strategic question to think through
outputs:
- At most five bullets on what the board collectively failed to consider, written before the recommendation.
- 'Round 1 — one per advisor: opening position, analysis, projections, vote, and one question for the board.'
- Round 2 — one per advisor, answering the other position papers.
- board-decision-html (html)
- board-decision-md (markdown)
- board-decision-pdf (pdf)
- decision-brief (markdown)
- '{scope.decisions}/{decision-slug}/round-1/{advisor-slug}.md'
- '{scope.decisions}/{decision-slug}/round-2/chair-bias-check.md'
- '{scope.decisions}/{decision-slug}/round-2/{advisor-slug}-rebuttal.md'
- '{scope.decisions}/{decision-slug}/{decision-slug}-board-decision.html'
- '{scope.decisions}/{decision-slug}/{decision-slug}-board-decision.md'
- '{scope.decisions}/{decision-slug}/{decision-slug}-board-decision.pdf'
- '{scope.decisions}/{decision-slug}_decision_brief.md'
prompts:
- ask boardroom
- ask the board
- sparring
- spar with me
---

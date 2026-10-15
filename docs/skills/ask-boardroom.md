---
description: Simulate a board of strategic advisors to debate your toughest business decisions.
title: ask-boardroom
---

# ask-boardroom

Simulate a board of strategic advisors to debate your toughest business decisions.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | business |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder] |

Simulate a board of advisors for strategic decisions, or run 1:1 strategic sparring sessions.

## How you ask

- “ask boardroom”
- “ask the board”
- “sparring”
- “spar with me”

## Inputs

- request — What to produce
- scope — `company`, or a client-id resolving to the client's folder (`client.root`) — a string with one reserved value, not a closed set
- decision — The decision or strategic question to think through

## Outputs

- At most five bullets on what the board collectively failed to consider, written before the recommendation.
- Round 1 — one per advisor: opening position, analysis, projections, vote, and one question for the board.
- Round 2 — one per advisor, answering the other position papers.
- board-decision-html (html)
- board-decision-md (markdown)
- board-decision-pdf (pdf)
- decision-brief (markdown)
- {scope.decisions}/{decision-slug}/round-1/{advisor-slug}.md
- {scope.decisions}/{decision-slug}/round-2/chair-bias-check.md
- {scope.decisions}/{decision-slug}/round-2/{advisor-slug}-rebuttal.md
- {scope.decisions}/{decision-slug}/{decision-slug}-board-decision.html
- {scope.decisions}/{decision-slug}/{decision-slug}-board-decision.md
- {scope.decisions}/{decision-slug}/{decision-slug}-board-decision.pdf
- {scope.decisions}/{decision-slug}_decision_brief.md

## Seen in these workflows

- [Stuck on a strategic decision.](../workflows/ask-boardroom.md)


---
description: Help a PM decide what promotion target to pursue, identify the evidence gap, and turn that gap into a concrete development plan.
title: career-growth
---

# career-growth

Help a PM decide what promotion target to pursue, identify the evidence gap, and turn that gap into a concrete development plan.

- **Area:** People
- **Category:** human resources
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Plans PM career advancement, identifies skill gaps, and structures promotion cases with gap analysis.

## How you ask

- “Help me build a promotion case for senior PM”
- “Identify my skill gaps for transitioning to management”
- “Plan my career growth path from IC to director level”
- “Should I go into management or stay as an IC?”

## Inputs

- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- career-growth (markdown)
- {scope.knowledge-base.product}/career-growth-{YYYY-MM-DD}.md


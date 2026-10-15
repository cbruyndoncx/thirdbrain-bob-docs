---
description: Generate a personalized morning digest consolidating emails, calendar, messages, and research alerts into a single actionable summary.
title: daily-briefing
---

# daily-briefing

Generate a personalized morning digest consolidating emails, calendar, messages, and research alerts into a single actionable summary.

- **Area:** Foundational
- **Category:** productivity
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** CEO / Founder

Generate a personalized morning briefing by aggregating emails, calendar events, Slack messages, and tracked research topics.

## How you ask

- “Give me my morning briefing”
- “What do I need to know today?”
- “Summarize my emails, calendar, and Slack from last night”
- “Generate today's daily digest”

## Inputs

- current_state — Weekly Priorities and Decisions Needed. Warn the owner when last_weekly_review is older than 10 days.

## Outputs

- briefing (markdown)
- {me.inbox}/briefing-{YYYY-MM-DD}.md


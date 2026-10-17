---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: daily-briefing — ThirdBrain BOB skill
  description: Generate a personalized morning digest consolidating emails, calendar, messages, and research alerts into a single actionable summary.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: daily-briefing
catLabel: productivity
area: foundational
desc: Generate a personalized morning briefing by aggregating emails, calendar events, Slack messages, and tracked research topics.
summary: Generate a personalized morning digest consolidating emails, calendar, messages, and research alerts into a single actionable summary.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[CEO / Founder]'
inputs:
- current_state — Weekly Priorities and Decisions Needed. Warn the owner when last_weekly_review is older than 10 days.
outputs:
- briefing (markdown)
- '{me.inbox}/briefing-{YYYY-MM-DD}.md'
prompts:
- Give me my morning briefing
- What do I need to know today?
- Summarize my emails, calendar, and Slack from last night
- Generate today's daily digest
---

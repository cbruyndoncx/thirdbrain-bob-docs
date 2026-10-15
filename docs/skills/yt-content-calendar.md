---
description: YouTube scheduling strategist. Build and maintain publishing calendars that balance content pillars, batch recording sessions, and seasonal opportunities. Consistency is the single biggest predictor of YouTube growth — a good calendar is what makes consistency sustainable.
title: yt-content-calendar
---

# yt-content-calendar

YouTube scheduling strategist. Build and maintain publishing calendars that balance content pillars, batch recording sessions, and seasonal opportunities. Consistency is the single biggest predictor of YouTube growth — a good calendar is what makes consistency sustainable.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | content |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Plan and manage YouTube publishing schedules with content pillar balance, batch recording cadence, and seasonal planning.

## How you ask

- “Content calendar”
- “Publishing schedule”
- “Plan my videos”

## Inputs

- planning_period — Period to plan, at most 8 weeks — e.g. 'next 4 weeks', 'May 2026'
- youtube_context — Channel context (`company.marketing`)
- existing_ideas — Video ideas to slot into the calendar — from yt-idea-generation or user input
- events — Upcoming events, launches, or seasonal dates to plan around
- existing_calendar — Current calendar file (`company.marketing`, calendar subfolder)
- performance_notes — Which videos performed above/below average, any missed slots
- schedule_changes — New events, shifted priorities, or slot swaps to incorporate

## Outputs

- Content calendar with weekly tables, pillar balance check, batch schedule, and production milestones
- Updated calendar with adjustment notes and rebalanced pillars
- {company.marketing}/video/calendar/yt_content_calendar_{YYYY-MM-DD}.md


---
description: Bridge between Google Calendar and the vault. Schedule meetings with vault-aware context, sync calendar events into meeting notes, check availability, and prep for the week ahead.
title: booking-scheduler
---

# booking-scheduler

Bridge between Google Calendar and the vault. Schedule meetings with vault-aware context, sync calendar events into meeting notes, check availability, and prep for the week ahead.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | productivity |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Schedules meetings in Google Calendar, checks availability, and prepares upcoming calls.

## How you ask

- “Book a meeting with Sarah for next Tuesday at 2pm”
- “Sync my Google Calendar with the vault”
- “Check my availability for Thursday afternoon”
- “Prep materials for my upcoming meetings this week”

## Inputs

- meeting_template — Meeting entity template used to create the vault note for the newly booked call.
- meeting_template — Meeting entity template used to pre-populate the agenda when a synced event has no existing vault note.
- request — Who to find time with and over what window. Absent a window, the route defaults to the next 5 business days; absent names, it checks the user's calendar only.
- booking_config — Working hours, buffer rules and minimum notice period used to filter raw free/busy blocks into offerable slots.
- request — Which meeting to act on — by attendee, date or title — and whether to reschedule or cancel it. Ambiguous matches are resolved by asking, not guessed.
- booking_config — Working hours and buffer rules applied when the reschedule branch re-runs availability for the same attendees.
- profile — Company or client profile used to enrich client meetings with sector and deal-stage context in the weekly view.

## Outputs

- Day-by-day calendar with prep items per meeting and flags for meetings without vault notes, unknown attendees, or back-to-back conflicts.
- First-use scheduling config (account, working hours, buffers, defaults), written once during preflight if it does not already exist.
- Vault meeting note created (new event) or updated in frontmatter only (existing event) for each synced calendar event.
- Vault meeting note created for the booked call, with wikilinked attendees and a default agenda from the detected meeting type.
- Vault meeting note whose frontmatter (date, time, or status) is updated to match the rescheduled or cancelled calendar event.
- {client.meetings}/{YYYY-MM-DD}_{title_slug}.md
- {company.operations}/calendar-review/{YYYY-MM-DD}_weekly_calendar.md
- {company.profile-root}/calendar/booking_config.md


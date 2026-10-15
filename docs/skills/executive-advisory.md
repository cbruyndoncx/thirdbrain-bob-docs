---
description: Strategic coaching and advisory operating system for executives — CXOs, founders, business heads, transformation leaders. Runs the full advisory lifecycle from intake through session, debrief, and burnout monitoring; serves both the advisor delivering the engagement and the leader using it as a thinking partner.
title: executive-advisory
---

# executive-advisory

Strategic coaching and advisory operating system for executives — CXOs, founders, business heads, transformation leaders. Runs the full advisory lifecycle from intake through session, debrief, and burnout monitoring; serves both the advisor delivering the engagement and the leader using it as a thinking partner.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | business |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder] |

Strategic coaching and advisory for executives navigating growth, influence, and transformation.

## How you ask

- “Run an executive intake on `acme-corp` — the CEO is dealing with board pressure on a pivot”
- “He says he needs strategy but I think he needs accountability — run hybrid detection”
- “Help me think through this difficult conversation with my chair”
- “Debrief our session — themes, risks, what to recommend next”
- “Is this exec burning out? Here's what I'm seeing: [signals]”

## Inputs

- client_id — Client slug (`client.root`) — the leader being onboarded
- context_notes — What the advisor already knows about the leader (role, business, presenting issue)
- request — The exact words the leader used (or summary of what they said they need)
- client_id — Client slug if running in advisor mode against a known leader
- client_id — Leader's slug; if self-use, omit and write to the personal workspace (`me.meetings`)
- topic — What the session is about — decision, tension, stakeholder, communication
- client_id — Client slug
- session_notes — Raw session notes or transcript from the advisor
- client_id — Leader's slug; if self-use, omit
- signals — Observed signals from recent sessions, calendar, communication patterns, behavior shifts

## Outputs

- discovery-intake (markdown)
- hybrid-detection-brief (markdown)
- readiness-assessment (markdown)
- session-debrief (markdown)
- session-notes (markdown)
- {client.feedback}/debrief_{YYYY-MM-DD}.md
- {client.feedback}/readiness_{YYYY-MM-DD}.md OR {me.meetings}/readiness_{YYYY-MM-DD}.md
- {client.feedback}/session_{YYYY-MM-DD}.md OR {me.meetings}/session_{YYYY-MM-DD}.md
- {client.profile-root}/executive_discovery_{YYYY-MM-DD}.md
- {client.profile-root}/hybrid_detection_{YYYY-MM-DD}.md OR {me.inbox}/hybrid_detection_{YYYY-MM-DD}.md


---
description: Produce clean, complete end-of-engagement documentation so clients receive a clear picture of what was delivered, what wasn't, how to use what they have, and what needs their formal sign-off. No project management tooling required — works from conversation context, existing files, and a short intake.
title: client-handoff
---

# client-handoff

Produce clean, complete end-of-engagement documentation so clients receive a clear picture of what was delivered, what wasn't, how to use what they have, and what needs their formal sign-off. No project management tooling required — works from conversation context, existing files, and a short intake.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Packages deliverables for client handoff with transition documents, sign-off checklists, knowledge transfer summaries, and coworker context briefs.

## How you ask

- “Package up the deliverables for the Acme project handoff”
- “Create a sign-off checklist for the client to approve”
- “Write a knowledge transfer doc so the client's team can maintain what we built”
- “Prepare end-of-engagement documentation for the website redesign project”
- “What do I send the client at the end of a project?”
- “Brief Sarah on the Acme project so she can take over”
- “Coworker handoff for the website redesign — I'm going on leave”
- “Hand off the Acme engagement to my colleague”

## Inputs

- request — What to produce
- project-context — Client folder (`client.root`) — Any existing project notes, scopes, or deliverable lists
- handoff-package — Handoff package (`client.handoff`) — Deliverable inventory from route-a
- project-context — Client folder (`client.root`) — Any existing project notes or deliverable files
- project-context — Client folder (`client.root`) — Any existing project notes, deliverables, or meeting history

## Outputs

- Fallback handoff pack, used when no client context is available.
- coworker-handoff (markdown)
- handoff-package (markdown)
- knowledge-transfer (markdown)
- prefer a permanent directory)
- sign-off-checklist (markdown)
- {client.handoff}/coworker_handoff.md
- {client.handoff}/handoff_package.md
- {client.handoff}/knowledge_transfer.md
- {client.handoff}/sign_off_checklist.md


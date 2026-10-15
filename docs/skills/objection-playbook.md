---
description: Generate comprehensive objection response scripts with word-for-word ready-to-use responses. Covers 15 universal objections, industry-specific objections, competitive objections, pricing deep-dives, and prevention techniques.
title: objection-playbook
---

# objection-playbook

Generate comprehensive objection response scripts with word-for-word ready-to-use responses. Covers 15 universal objections, industry-specific objections, competitive objections, pricing deep-dives, and prevention techniques.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Sales] |

Generate competitor-specific objection handling playbooks.

## How you ask

- “Create an objection playbook for competing against Salesforce”
- “How do I counter the 'too expensive' objection?”
- “Generate word-for-word responses for our top 5 deal objections”
- “Build a competitive objection handling guide for the sales team”

## Inputs

- scope — `company` (default), or a client-id under {company.clients}/ passed explicitly by the runner when the playbook is for a client's sales team; decides the output folder
- industry — Sector whose common objections are being handled
- competitors — Competitors whose positioning drives the objections
- icp — ICP — anchors objections against the target buyer profile.
- offerings — Offerings catalogue — scopes pricing and feature objections.
- marketing-context — Positioning context — frames differentiation answers.
- prospect — Specific prospect the playbook is for
- known_objections — Objections already raised in conversation
- transcripts — Two or more transcripts of calls that did NOT close. One call is an anecdote; the pattern only appears across several
- outcome_notes — Recorded loss reasons, where they exist — used to check the transcript reading against what was believed at the time

## Outputs

- objection-playbook (markdown)
- {scope.sales}/objection-playbooks/from-failed-calls-{YYYY-MM-DD}.md
- {scope.sales}/objection-playbooks/{competitor-or-industry}.md
- {scope.sales}/objection-playbooks/{industry}.md


---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: personal-context-builder — ThirdBrain BOB skill
  description: USE WHEN user says "build my profile", "personal context", "who am I", "my values", "my life context", "constitution", "personal life", or wants AI to understan
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: personal-context-builder
catLabel: productivity
area: foundational
desc: Build deep personal context files through guided interview.
summary: USE WHEN user says "build my profile", "personal context", "who am I", "my values", "my life context", "constitution", "personal life", or wants AI to understand them better.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- existing-constitution — The constitution already on disk, read before anything is written so the user can choose to extend it, start fresh, or read it back first.
- transcript — Voice-memo transcript answering the interview questions. Absent, the route runs the interview live, one question at a time.
- file-action — What to do when the file already exists. The choice decides whether prior answers are extended, discarded, or only read back to the user before any write happens. (update | replace | review)
- depth — Interview length. The shortened setting asks three questions instead of five to eight and produces a minimal but usable file, and the user is told it can be deepened later. (full | quick)
- sensitivity — Privacy level the user wants respected in the written file — what may be recorded verbatim and what must be generalised or left out.
- existing-personal-life — The personal life file already on disk, read before anything is written so the user can choose to extend it, start fresh, or read it back first.
- sensitivity — Privacy level the user wants respected in the written file — health, family and employer detail are the recurring cases.
- transcript — Voice-memo transcript covering both interviews. Absent, the route runs them live, one question at a time.
- file-action — What to do when either file already exists. The choice decides whether prior answers are extended, discarded, or only read back to the user before any write happens. (update | replace | review)
- depth — Interview length. The shortened setting asks three questions per file instead of five to eight and produces minimal but usable files, and the user is told they can be deepened later. (full | quick)
- sensitivity — Privacy level the user wants respected in the written files — what may be recorded verbatim and what must be generalised or left out.
- context-source — constitution supplies Worldview, personal_life supplies Backstory, profile supplies Identity. At least one of the first two must already exist — this route reformats existing context and runs no interview.
- scope — `personal` (default), `company`, or a client-id under {company.clients}/
- slug — Persona filename slug
outputs:
- Daily rhythms, what fills versus depletes, quirks and constraints, and the gap between the ideal day and the real one.
- Values, non-negotiables and the trade-offs between them, in the user's own voice, with unresolved tensions left visible rather than smoothed.
- Values, non-negotiables and the trade-offs between them, in the user's own voice.
- persona (markdown)
- '{me.constitution}'
- '{me.personas}/{slug}.md'
- '{me.profile-root}/personal_life.md'
prompts:
- Build my personal profile for better AI interactions
- Define my values and working style preferences
- Create my life context document with daily rhythms and energy patterns
- Help AI understand me better — run the guided interview
---

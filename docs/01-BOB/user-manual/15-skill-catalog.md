---
description: Representative skills grouped by business area, with what each is for
  and when to reach for it
title: BOB User Manual — 15. The Skill Catalog
---

# 15. The Skill Catalog

A **skill** is a packaged workflow for one business job — with defined inputs, steps, quality checks, and a defined output. The full BOB release (v2.8.0) ships over 380 skills; a starter vault stores 14 and receives the rest from the skills server or the free skill packs (see [chapter 14](14-skills-system.md)). You don't memorise them: describe what you want in plain words and BOB routes to the right one. This section shows the shape of the library through representative examples per area.

> **How invocation works**
> A skill name like `/proposal-writer` is just the fastest path. Describing the job in plain English works equally well — BOB figures out the routing. The complete, always-current index is [SKILLS](../../skills/index.md) at the vault root. In a starter vault that index lists only the local skills; ask BOB "search for a skill that does ..." and it queries the skills server. A skill that is not stored locally is read from the server, so it can be used the same way. The skills were audited against the QMS gate for v2.8.0; what that means and where to inspect it is in [chapter 14](14-skills-system.md).

## Sales & Growth

| Skill | What it does | When |
|-------|--------------|------|
| `lead-qualifier` | Scores a lead against your ideal customer profile | A new prospect appears |
| `proposal-writer` | Interviews you about a deal, drafts the proposal | You need to send a proposal |
| `sales-pipeline-report` | Aggregates deals into a pipeline health report | Weekly or before a review |
| `cold-email` / `linkedin-outreach` | Drafts outreach in your voice | Starting a campaign |
| `crm-pipeline` | Keeps leads, deals, and contacts organised | Ongoing |

## Marketing & Content

| Skill | What it does | When |
|-------|--------------|------|
| `social-content` | Writes LinkedIn/X/Substack posts from your material | Regular publishing |
| `content-repurposer` | Turns one piece of content into many formats | You have a good article or talk |
| `seo-audit` / `website-audit` | Scores your site and lists concrete fixes | Quarterly, or before a relaunch |
| `brand-voice-generator` | Captures your tone so drafts sound like you | Once, early on |

## Finance & Administration

| Skill | What it does | When |
|-------|--------------|------|
| `invoice-collector` / `ar-followup` | Tracks receivables, drafts payment reminders | Monthly |
| `financial-reporting` | Produces management-ready financial summaries | Period end |
| `period-close-orchestrator` | Walks the full close, step by step | Month/quarter end |
| `quotation-generator` | Builds priced quotes from your catalog | A deal needs numbers |

## Operations & Projects

| Skill | What it does | When |
|-------|--------------|------|
| `meeting-intelligence` | Extracts decisions, actions, and risks from meeting notes | After every important meeting |
| `project-status` / `project-charter` | Standard PM artifacts from your project data | Running client or internal projects |
| `process-kaizen` | Maps a process and finds the waste in it | Something feels inefficient |
| `root-cause-analysis` | Structured five-why / fishbone analysis | Something went wrong |

## Strategy & Management

| Skill | What it does | When |
|-------|--------------|------|
| `ask-boardroom` | Simulates a board of advisors debating your decision | A big call with real trade-offs |
| `decision-frameworks` | Expected value, pre-mortem, structured choices | Recurring decisions |
| `market-sizing-analysis` | Estimates a market opportunity with sources | Entering a new segment |
| `weekly-review` / `daily-briefing` | Your operating rhythm — priorities in, noise out | Every day / week |

## Documents & Deliverables

| Skill | What it does | When |
|-------|--------------|------|
| `docx-tools` / `xlsx-tools` / `pptx-tools` | Reads and produces Word, Excel, PowerPoint | Client-facing office documents |
| `branded-pdf` / `pdf-report` | Renders on-brand PDF deliverables and reports | Anything you'd hand to a client |
| `excalidraw-diagrams` / `drawio` | Flowcharts, architecture and process diagrams | A picture beats a paragraph |

## What every skill has in common

- **Defined inputs and outputs** — it tells you what it needs and what you'll get
- **Vault-aware** — it reads your real business context, not a blank slate
- **Draft discipline** — outward-facing results wait for your approval
- **Quality gates** — governed skills carry acceptance criteria that the output is checked against


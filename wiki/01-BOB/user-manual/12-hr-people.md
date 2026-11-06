---
type: knowledge-base
title: "BOB User Manual — 12. HR & People"
description: "How BOB supports the full hire-to-productivity journey: people records, recruiting, onboarding, performance, growth, and delegation"
status: draft
created: 2026-08-07
modified: 2026-08-31
tags: [bob, user-manual, wiki]
---

# 12. HR & People

BOB's HR module covers the full **hire-to-productivity** journey — from deciding you need a role through recruitment, onboarding, and ongoing performance and development. People data lives in your vault as structured entities; skills handle the operational work against that data.

Payroll-adjacent records — gratuity accruals, WPS SIF files, and statutory filings — live in Finance. See [[10-finance|chapter 10, Finance & Administration]] for those.

---

## 12.1 People records

BOB tracks individuals as **Person entities** in the vault. Each person record holds contact details, role, reporting line, start date, and the client or internal scope the person belongs to.

| Field | What it holds |
|-------|--------------|
| Name, role, department | Identity and org-chart position |
| Scope | `internal` for your own staff; `client:{name}` for contacts at a client organisation |
| Status | `active`, `candidate`, `alumni` |
| Linked notes | Onboarding doc, performance reviews, 1:1 logs |

Person records are created automatically when you run `hiring`, `employee-onboarding`, or `create-client`. You can also create them manually. Keep the `scope` field accurate — it controls which data surfaces in client-facing views versus internal ones.

---

## 12.2 Recruiting

The recruiting workflow begins before you write a job post. Use `team-composition-analysis` first to pressure-test the decision: it maps your current headcount, identifies structural gaps, and produces a hiring-plan brief with role priorities, comp assumptions, and equity ranges.

Once the role is confirmed, `hiring` manages the full pipeline.

### Recruiting workflow — step by step

| Step | What you do | What BOB does | Where it's saved |
|------|-------------|---------------|-----------------|
| 1. Define the role | Describe the gap and seniority | Produces a role brief and competency list | Vault — People folder |
| 2. Write the job post | Review and approve the brief | Drafts job description for your chosen channel | Google Doc |
| 3. Design the interview | Confirm evaluation criteria | Creates a structured interview scorecard | Google Doc |
| 4. Evaluate a candidate | Paste or summarise interview notes | Scores the candidate against the scorecard; gives hire/no-hire recommendation | Vault — candidate note |
| 5. Make an offer | Approve the recommendation | Drafts offer letter with role, comp, and start date | Google Doc (via `employment-contract-templates`) |

For sourcing channels — outreach sequences, LinkedIn searches — see the sales and marketing skills (`linkedin-outreach`, `linkedin-searches`, `outbound-sequence`). `hiring` does not manage paid job-board spend.

**Good practice:** log every candidate as a Person entity with `status: candidate`. If they don't get the role, set `status: alumni`. This builds a pipeline you can return to without starting over.

---

## 12.3 Onboarding

`employee-onboarding` picks up where `hiring` leaves off. Trigger it after an offer is accepted.

### Onboarding workflow

| Step | What you do | What BOB does | Where it's saved |
|------|-------------|---------------|-----------------|
| 1. Trigger onboarding | Confirm name, role, and start date | Creates a structured onboarding plan | Google Doc |
| 2. Review the plan | Edit tool access, key contacts, first tasks | — | — |
| 3. Assign a buddy | Name the buddy in the doc | Adds buddy context to the first-week schedule | Google Doc |
| 4. Track 30/60/90 milestones | Check in at each milestone | Generates 30/60/90-day check-in agendas on request | Google Doc |

The onboarding doc links back to the Person entity. When the 90-day plan is complete, update the Person record's `status` to `active` and link any completed documents.

**Good practice:** run `performance-review` at the 90-day mark — the same skill used for ongoing reviews — rather than treating probation as a one-off. It keeps the format consistent and creates a baseline for later reviews.

---

## 12.4 Performance and growth

BOB supports three types of performance-related work: structured reviews, regular 1:1s, and longer-range career development.

### Skills at a glance

| Skill | When to use it |
|-------|---------------|
| `performance-review` | Formal reviews, probation check-ins, 90-day plans |
| `one-on-ones` | Weekly or fortnightly 1:1 preparation and facilitation |
| `career-growth` | Career conversations, promotion cases, skill-gap planning for an individual |
| `skill-gap-analysis` | Auditing skill coverage across the team or a role |

### Performance review workflow

| Step | What you do | What BOB does | Where it's saved |
|------|-------------|---------------|-----------------|
| 1. Initiate review | Name the person and review period | Generates a review template with agreed goals, ratings, and development section | Google Doc |
| 2. Gather input | Add your notes; optionally paste the person's self-assessment | Structures both into the review format | Google Doc |
| 3. Hold the conversation | Use the doc as your agenda | — | — |
| 4. Log outcomes | Record agreed actions in the doc | Links completed review to the Person entity | Vault |

### 1:1 workflow

Tell BOB "prep my 1:1 with [name]" and it reads the Person entity, recent meeting notes, and any open tasks linked to that person. It returns a structured agenda. After the meeting, paste back the key points and BOB logs them to a 1:1 note linked to the person record.

`career-growth` is longer-range. Use it when a team member is working toward a promotion or a role transition. It produces a gap analysis against the target role and a structured development plan.

---

## 12.5 Delegation and accountability

`delegation` is for founders and managers who are bottlenecked. It audits how you're spending your time, sorts tasks into four buckets, and builds handoff plans.

| Bucket | What it means |
|--------|--------------|
| Only You | Must stay with you — judgment, relationships, vision |
| Teach Someone | You can do it, but someone else can learn it |
| Hire For | Requires a role that doesn't exist yet |
| Eliminate | Should stop happening entirely |

The output is a delegation brief per task, including a "good enough" standard so the person taking it over knows what success looks like. This connects directly to `team-composition-analysis` — if the audit surfaces a Hire For bucket, that feeds the next recruiting cycle.

**Good practice:** run `delegation` quarterly, not just when you're overwhelmed. Catching bottlenecks early is cheaper than firefighting them.

---

## 12.6 HR operations

`hr-ops` covers recurring HR documentation that doesn't fit the other workflows: training module outlines, policy templates, curriculum design, and people-ops documentation. Use it for anything that needs a well-structured document rather than a decision or a plan.

`team-status-generator` turns project and task activity into a team status update or standup summary, so you can see what each person moved without asking. `time-tracking-reporter` turns time logs into utilization reports — useful during probation or when managing remote contributors.

---

## 12.7 Skills serving this module

| Skill | Value chain stage |
|-------|------------------|
| `team-composition-analysis` | need |
| `hiring` | recruit |
| `employment-contract-templates` | hire |
| `employee-onboarding` | onboard |
| `performance-review` | perform |
| `team-status-generator` | perform |
| `time-tracking-reporter` | perform |
| `one-on-ones` | develop |
| `career-growth` | develop |
| `skill-gap-analysis` | develop |
| `delegation` | cross-cutting |
| `hr-ops` | cross-cutting |

**Playbook:** [[Hire-to-Productivity]] chains these stages end to end. Run it for a new hire rather than triggering skills individually.

---

## 12.8 Good practices

- Keep Person entities current. Stale records produce wrong answers when BOB reads the vault for context.
- Use `status: candidate` consistently. It lets you search your pipeline without cluttering the active staff list.
- Link every HR document back to the Person entity. Reviews, onboarding plans, and 1:1 logs are most useful when connected to a single record.
- Payroll is not here. Gratuity calculations, WPS files, and contract statutory clauses live in [[10-finance|chapter 10, Finance & Administration]].


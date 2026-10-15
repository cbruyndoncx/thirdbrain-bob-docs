---
description: 'Computes the owner''s Buy Back Rate — the dollar value of one hour of their time — then turns a two-week time-and-energy audit into a ranked list of exactly which tasks to offload first, routing each to AI/automation before a human hire. It is the quantitative front-end to delegation: `delegation` coaches the human handoff; this skill produces the number and the ranked target list that tell you *what* to hand off and *to what*.'
title: buyback-rate
---

# buyback-rate

Computes the owner's Buy Back Rate — the dollar value of one hour of their time — then turns a two-week time-and-energy audit into a ranked list of exactly which tasks to offload first, routing each to AI/automation before a human hire. It is the quantitative front-end to delegation: `delegation` coaches the human handoff; this skill produces the number and the ranked target list that tell you *what* to hand off and *to what*.

- **Area:** Foundational
- **Category:** productivity
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Operations Manager

Computes your Buy Back Rate and turns a time-and-energy audit into a ranked 'offload this first' list — routing each task to automate-with-AI before hire.

## How you ask

- “What's my time worth”
- “What should I stop doing”
- “Buy back my time”

## Inputs

- income — Annual income basis = profit + owner salary + business expenses (the value the owner's 2,000 working hours produce).
- time_log — A task time-log (manual table, or exported from ai-work-audit / time-tracking-reporter). One row per recurring task with rough weekly hours.
- income — Income basis for the rate. If omitted, the audit reports relative ranking only (no dollar threshold).

## Outputs

- offload-report (markdown)
- prefer a permanent directory)
- rate-brief (markdown)


---
description: Automated lead qualification engine using BANT and MEDDIC frameworks. Evaluates prospects against proven sales qualification criteria using publicly available information.
title: lead-qualifier
---

# lead-qualifier

Automated lead qualification engine using BANT and MEDDIC frameworks. Evaluates prospects against proven sales qualification criteria using publicly available information.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Sales

Automated lead qualification using BANT and MEDDIC frameworks.

## How you ask

- “Qualify this lead using BANT scoring”
- “Score this prospect with a MEDDIC assessment”
- “Is this lead worth pursuing? Run a full qualification”
- “Rate the opportunity quality for this incoming inquiry”

## Inputs

- lead — Lead details — company, contact, source, and any discovery notes
- framework — Qualification framework to score against — bant, meddic, or both. Omit for the skill's default; use meddic for complex enterprise deals. (bant | meddic | both)
- icp — ICP definition used to score fit and need.
- offerings — Offerings catalogue used to score interest and budget fit.
- lead — Lead details supplied by the calling skill
- calling_skill — Skill invoking this one, which sets the output shape
- member-export — Skool member-export CSV, exported manually from the Skool admin UI
- community — Skool community slug, recorded on each emitted lead

## Outputs

- lead-file (markdown)
- lead-qualification (markdown)
- triage-digest (markdown)
- {client.sales}/lead_qualification.md
- {lead.profile}
- {lead.root}/{lead-id}.md
- {me.inbox}/skool_member_import_{YYYY-MM-DD}.md


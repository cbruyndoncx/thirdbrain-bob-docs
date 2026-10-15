---
description: Turn post engagement into a worked lead list — without scraping anything.
title: linkedin-engager-leads
---

# linkedin-engager-leads

Turn post engagement into a worked lead list — without scraping anything.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Head of Sales] |

Turns a pasted list of people who reacted to or commented on a LinkedIn post into a scored, deduplicated warm-lead sheet with a compliant first-contact line.

## How you ask

- “Here's who reacted to my close-process post — qualify them”
- “Turn this reaction list into warm leads, and flag anyone who engaged before”
- “Marc asked me not to contact him again — suppress him”

## Inputs

- eu_outreach_compliance — EU cold-outreach compliance rules. Every first message must carry the four elements it defines.
- paste — Text copied from the post's reactions or comments panel
- post — The post they engaged with, quoted well enough to reference in outreach
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- sheet — Path to an engager sheet produced by the qualify route
- selection — Which grades to draft for; defaults to A and B only
- person — Name exactly as it appears on LinkedIn; company, if known, goes in the reason comment, not on the name line
- reason — Free text — how the objection arrived. Kept as the compliance record.

## Outputs

- Cumulative engager history for company scope; the merge base for the next run, rewritten by the parser
- Cumulative engager history for one client scope; the merge base for the next run, rewritten by the parser
- engager-sheet (markdown)
- engager-sheet-client (markdown)
- first-contact-drafts (markdown)
- suppression-list (markdown)
- {client.sales}/engager-history.json
- {client.sales}/engager-leads-{YYYY-MM-DD}.md
- {company.sales.sequences}/engager-openers-{YYYY-MM-DD}.md
- {company.sales}/engager-history.json
- {company.sales}/engager-leads-{YYYY-MM-DD}.md
- {company.sales}/suppression-list.md


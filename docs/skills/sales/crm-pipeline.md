---
description: Obsidian-native sales pipeline management. Track deals through stages, log activities, review pipeline health, and never lose a follow-up.
title: crm-pipeline
---

# crm-pipeline

Obsidian-native sales pipeline management. Track deals through stages, log activities, review pipeline health, and never lose a follow-up.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Head of Sales

Manages the client deal pipeline as vault deal notes — stage moves, reviews, new prospects, health metrics, activity logs, partner rollups.

## How you ask

- “Update the pipeline stage for the Acme Corp deal”
- “Review all deals in the negotiation stage”
- “Add a new prospect to our sales pipeline”
- “Run a pipeline health report for this quarter”

## Inputs

- deals — Deal notes for the client — the one being moved is read in full before any field is changed.
- profile — Company or client profile — relationship context used to judge whether the transition is credible.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- target-stage — Stage the deal moves to. The choice sets the default probability and the suggested next action, and movement is forward-only unless the deal is being closed out. (lead | lost | negotiation | proposal | qualified | won)
- transition-note — One-line reason for the move, recorded verbatim in the activity entry so the stage history stays readable later.
- deals — Open deal notes scanned for stage, value, probability, next action, and last contact.
- all-clients — Widens the scan from the active client to every client folder. Requires explicit operator confirmation and is stated in the report header.
- deal-template — Template the new deal note is built from, so every deal starts with the same required frontmatter.
- company-name — Prospect company the deal belongs to; resolves the client folder or triggers its creation.
- contact-name — Primary contact recorded on the new deal.
- deal-source — How the lead reached the business. The value drives source-mix analysis in later reviews, so a guess here is worse than asking. (direct | event | existing-client | inbound | outbound | partner | referral)
- deal-value — Estimated amount in the primary currency. Left empty, the deal is flagged as unvalued in the next review.
- expected-close — Expected close date used for forecasting and ageing.
- deals — Deal notes scanned for stage distribution, ageing, top deals, and dated commitment bullets.
- prior-run-state — Per-deal streak state from the previous run, read back so a deal missing its next action across consecutive runs can be flagged rather than re-reported as new.
- no-state — Suppresses the state write so dry runs and tests do not consume a streak slot.
- deals — Deal notes; the one being touched is identified before anything is appended.
- transcript — Meeting transcript or call notes the activity summary is written from when the operator does not dictate it directly.
- activity-type — Class of touch being recorded; it labels the activity-log line. Skill-local — unrelated to `activity.channel`. (call | email | meeting | demo | proposal | follow-up)
- activity-note — One-line description of what happened, appended verbatim to the activity log.
- next-action — New due date for the follow-up. Omitted, the existing next action stands unchanged.
- partner-profiles — Partner profiles — status, relationship type, agreement type, open questions.
- partner-agreements — Agreement notes whose `status:` sets the recorded agreement state.

## Outputs

- Deal note with refreshed last-contact date and a new activity-log entry appended.
- Generated per-deal streak state for consecutive-report flagging. Never hand-edited.
- New deal note at stage lead with required frontmatter and an initialised activity log.
- Per-partner agreement state, blocking items quoted from source notes, and a Data Gaps section for folders with no partner note.
- Stage-grouped table of open deals with total and weighted pipeline value, plus the stale and actionless deals called out. Overwritten on each run.
- Summary metrics, stage breakdown, ageing, alerts, top deals, overdue commitments, and repeat next-action gaps.
- Updated deal note carrying the new stage, probability, last contact, next action, and an appended activity entry.
- {client.deals}/{deal_name}.md
- {company.partners}/REPORTS/partner_agreement_status_{YYYY-MM-DD}.md
- {company.sales}/pipeline_health_{YYYY-MM}.md
- {company.sales}/pipeline_report_state.json
- {company.sales}/pipeline_review.md


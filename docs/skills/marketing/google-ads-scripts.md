---
description: Develop Google Ads Scripts using the AdsApp API for campaign automation, bid optimization, performance reporting, and bulk operations.
title: google-ads-scripts
---

# google-ads-scripts

Develop Google Ads Scripts using the AdsApp API for campaign automation, bid optimization, performance reporting, and bulk operations.

- **Area:** Marketing
- **Category:** marketing ads
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** Head of Marketing

Guides Google Ads Scripts development with AdsApp API, campaign management, keyword bids, automated rules, and performance reporting.

## How you ask

- “Create a Google Ads script to pause low-performing keywords”
- “Build an automated bid adjustment script based on ROAS”
- “Write a script to generate a daily performance report”
- “Automate budget pacing across my Google Ads campaigns”

## Inputs

- request — The reporting need — which metrics, which date range, and where the output should land (Sheet, log, email).
- target-entity — Which Google Ads entity level the report reads from; determines the selector and available stats. (campaign | ad-group | keyword | ad | account)
- account-context — Existing campaign structure and scripts for this account, read to match naming conventions and avoid duplicating a report that already exists.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- request — The optimization goal — which metric drives the decision (ROAS, CPA, quality score), the target thresholds, and the entities in scope.
- target-entity — Which Google Ads entity level the script mutates; determines the selector, available setters, and blast radius of a mistake. (campaign | ad-group | keyword | ad | account)
- account-context — Existing campaign structure, conversion names, and scripts already deployed, read so the new bid or budget logic does not collide with them.
- request — The hygiene task — what to label, monitor, or clean up, and the condition that triggers the action.
- target-entity — Which Google Ads entity level the automation labels, monitors, or cleans up. (campaign | ad-group | keyword | ad | account)
- account-context — Existing labels, naming conventions, and scripts already in place, read so the new automation follows the same convention instead of introducing a second one.
- template — Which bundled template under `assets/` is the starting point; selects the base selectors and logic to customize. (bid-manager | campaign-optimizer)
- request — What the template needs to become — the entities, thresholds, and naming to substitute for this account.
- account-context — Existing campaign structure and scripts, read so the adapted template matches this account's naming and entity conventions.

## Outputs

- The monitoring, labeling, or cleanup automation, with the trigger condition and alerting/logging it performs.
- The mutating bid, budget, keyword, or status script, with its preview/validation logic and the threshold values it acts on.
- The read-only reporting or export script, with the date range, entity selectors, and destination it writes to.
- The template script adapted with this account's entities, thresholds, and naming.


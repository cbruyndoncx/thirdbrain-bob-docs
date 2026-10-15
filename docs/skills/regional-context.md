---
description: Refresh and maintain regional business environment intelligence files. Each region has a domain config (scope, queries, advisory context) and a `business-environment.md` output that business skills consume when working with clients in that region.
title: regional-context
---

# regional-context

Refresh and maintain regional business environment intelligence files. Each region has a domain config (scope, queries, advisory context) and a `business-environment.md` output that business skills consume when working with clients in that region.

| | |
|---|---|
| **Area** | Research |
| **Category** | research |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Refreshes regional business environment research for configured regions.

## How you ask

- “Refresh the UAE regional context”
- “Check which regions are stale”
- “Set up a new region for Saudi Arabia”
- “Refresh all stale regions”
- “What's changed in the India business environment since last refresh?”

## Inputs

- region_sector_overlay — Sector-specific overlay for the region, checked when one exists.
- region_changelog — Running change log for the region, read on refresh when it exists.
- operating-regions — Configured regions — the list this skill refreshes.
- region — Region ID (e.g., uae, india, australia)
- domain-config — loaded from your vault context
- current-environment — loaded from your vault context
- scope — Pass 'stale-only' to skip fresh regions, or omit to refresh all
- request — User request and source context for check-staleness
- region — Region ID to create (e.g., saudi-arabia, uk)

## Outputs

- The new-region route updates this list; the other routes only read it (declared as the `operating-regions` input).
- business-environment (markdown)
- business-environment-changelog (markdown)
- business-environment-snapshot (markdown)
- domain-config (markdown)
- refresh-report (markdown)
- region-briefing (markdown)
- staleness-report (markdown)
- {company.profile-root}/operating_regions.md
- {me.inbox}/regional_refresh_{YYYY-MM-DD}.md
- {me.inbox}/regional_{region}_{YYYY-MM-DD}.md
- {resource.regions}/{region}/business-environment.md
- {resource.regions}/{region}/business-environment_changelog.md
- {resource.regions}/{region}/business-environment_{YYYY-MM-DD}.md
- {resource.regions}/{region}/staleness-{YYYY-MM-DD}.md
- {resource.research-domains}/region-{region}.md

## Seen in these workflows

- [Regional Context](../workflows/regional-context.md)


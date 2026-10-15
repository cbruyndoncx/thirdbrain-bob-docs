---
description: Connects to a Skool community via the [Apify-hosted Skool All-in-One API actor](https://apify.com/cristiantala/skool-all-in-one-api). Read AND write to posts, comments, members, classroom (courses/folders/pages), files, and group settings — through a single HTTP endpoint, no browser automation.
title: skool-actor
---

# skool-actor

Connects to a Skool community via the [Apify-hosted Skool All-in-One API actor](https://apify.com/cristiantala/skool-all-in-one-api). Read AND write to posts, comments, members, classroom (courses/folders/pages), files, and group settings — through a single HTTP endpoint, no browser automation.

- **Area:** Foundational
- **Category:** integrations
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** api-key
- **Roles:** Content Manager

Read and write to a Skool community programmatically via the Apify-hosted Skool All-in-One API actor.

## How you ask

- “List the pending members in this Skool community without approving anyone.”
- “Publish this approved lesson body to the named course and verify the page tree.”
- “Create this approved community post after showing me the final plain-text content.”
- “Approve these exact memberIds and return the per-member actor results.”

## Inputs

- action — Supported read action plus group slug and required object identifiers.
- approved-content — User-approved action, target IDs, titles, body content, and group slug.
- member-action — Approved action, group slug, and exact memberId values returned by the actor.

## Outputs

- actor-result (json)
- member-result (json)
- prefer a permanent directory)
- publication-log (markdown)
- stdout


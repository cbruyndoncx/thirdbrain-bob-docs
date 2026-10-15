---
description: 'Full-stack SEO content pipeline: research, write, optimize, score, and publish.'
title: seo-content-machine
---

# seo-content-machine

Full-stack SEO content pipeline: research, write, optimize, score, and publish.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing seo |
| **Level** | advanced |
| **Input** | url |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Runs an end-to-end SEO content pipeline for WordPress.

## How you ask

- “Research keywords and write an optimized blog post”
- “Create an SEO-optimized landing page for our target keyword”
- “Analyze the SEO performance of our existing blog content”
- “Publish this article to WordPress with Yoast optimization”
- “Rewrite this blog based on the audit report”
- “The audit scored this 6.2 — rewrite targeting the weak areas”

## Inputs

- url — Target site URL — the site whose content is researched, rewritten, audited or published (performance research reads it as GSC_SITE_URL)
- scope — `company`, or a client-id under the client root (`client.root`) — a string with one reserved value, not a closed set
- marketing-context — Consolidated marketing context — one file with Target Audience, Customer Language, Differentiation, Problems & Pain Points, and Proof Points sections (assembled by product-marketing-context).
- icp — Deep ICP — buyer profile, scoring, and buying journey. Company uses icp.md; clients use ideal_customer_profiles_index.md (per-segment ICP files).
- brand-voice — Locked brand/tone-of-voice for on-voice drafting.

## Outputs

- seo-content-draft (markdown)
- seo-content-draft-client (markdown)
- seo-content-research (markdown)
- seo-content-research-client (markdown)
- {client.marketing.seo}/drafts/{topic-slug}-{YYYY-MM-DD}.md
- {client.marketing.seo}/research/brief-{topic-slug}-{YYYY-MM-DD}.md
- {company.marketing.seo}/drafts/{topic-slug}-{YYYY-MM-DD}.md
- {company.marketing.seo}/research/brief-{topic-slug}-{YYYY-MM-DD}.md

## Seen in these workflows

- [Content takes forever.](../workflows/seo-content-machine.md)


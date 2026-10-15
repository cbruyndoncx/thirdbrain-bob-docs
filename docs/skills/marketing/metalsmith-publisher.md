---
description: Use this skill for scoped changes to a Metalsmith-based website defined by a vault config note.
title: metalsmith-publisher
---

# metalsmith-publisher

Use this skill for scoped changes to a Metalsmith-based website defined by a vault config note.

- **Area:** Marketing
- **Category:** marketing seo
- **Level:** advanced
- **Input:** url
- **Output:** document
- **Setup:** config, install
- **Roles:** Head of Marketing

Maintains and updates Metalsmith static websites in this vault.

## How you ask

- “Update the homepage content on our Metalsmith site”
- “Fix the SEO metadata across all pages”
- “Change the SCSS styling for the navigation component”
- “Add a new service page to the website”

## Inputs

- source_note — Vault note to publish
- target_page — Site path to publish to; derived from the note when omitted
- component_name — Component to create or modify
- spec — Behaviour and props the component must support
- page_path — Page to optimize
- target_queries — Queries the page should rank for or be cited on

## Outputs

- seo-update (markdown)
- updated-component (markdown)
- updated-content (markdown)
- {company.marketing}/seo-audits/metalsmith-publisher-{YYYY-MM-DD}.md


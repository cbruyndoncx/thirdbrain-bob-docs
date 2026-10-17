---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: metalsmith-publisher — ThirdBrain BOB skill
  description: Use this skill for scoped changes to a Metalsmith-based website defined by a vault config note.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: metalsmith-publisher
catLabel: marketing-seo
area: marketing
desc: Maintains and updates Metalsmith static websites in this vault.
summary: Use this skill for scoped changes to a Metalsmith-based website defined by a vault config note.
difficulty: advanced
inputType: url
outputType: document
requires: '[config, install]'
roles: '[Head of Marketing]'
inputs:
- source_note — Vault note to publish
- target_page — Site path to publish to; derived from the note when omitted
- component_name — Component to create or modify
- spec — Behaviour and props the component must support
- page_path — Page to optimize
- target_queries — Queries the page should rank for or be cited on
outputs:
- seo-update (markdown)
- updated-component (markdown)
- updated-content (markdown)
- '{company.marketing}/seo-audits/metalsmith-publisher-{YYYY-MM-DD}.md'
prompts:
- Update the homepage content on our Metalsmith site
- Fix the SEO metadata across all pages
- Change the SCSS styling for the navigation component
- Add a new service page to the website
---

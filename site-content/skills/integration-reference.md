---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: integration-reference — ThirdBrain BOB skill
  description: 'The vault''s catalogue of third-party tool integrations: what each tool offers (API, MCP, CLI, SDK), how authentication works, and what a working request looks l'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: integration-reference
catLabel: operations
area: operations
desc: Looks up how to connect to a third-party SaaS tool — auth type and scopes, whether an API, MCP server, CLI or SDK exists, and worked request examples — across 93…
summary: 'The vault''s catalogue of third-party tool integrations: what each tool offers (API, MCP, CLI, SDK), how authentication works, and what a working request looks like. Skills link here instead of restating connection detail that goes stale in a dozen places at once.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager, Operations Manager]'
inputs:
- tool — Tool name or slug, e.g. `stripe`, `Google Ads`, `customer-io`
- operation — The specific thing to do, e.g. 'list campaigns', 'create a contact' — narrows the answer to the relevant example
- check-only — Report staleness and exit non-zero instead of rewriting the index
- tool — Tool name to add
- source (Add Integration) — Where the integration facts come from — official API docs URL, or the vendor's MCP listing
outputs:
- integration-profile (markdown)
- new-integration (markdown)
- references/integrations/{tool}.md
- references/tool-index.md
- tool-index (markdown)
prompts:
- How do I authenticate against the Google Ads API?
- Does Klaviyo have an MCP server?
- Which of our catalogued tools expose a CLI?
- Which integrations does any skill actually use?
- Add Linear to the integration catalogue
---

---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skool-actor — ThirdBrain BOB skill
  description: Connects to a Skool community via the [Apify-hosted Skool All-in-One API actor](https://apify.com/cristiantala/skool-all-in-one-api). Read AND write to posts, c
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skool-actor
catLabel: integrations
area: foundational
desc: Read and write to a Skool community programmatically via the Apify-hosted Skool All-in-One API actor.
summary: Connects to a Skool community via the [Apify-hosted Skool All-in-One API actor](https://apify.com/cristiantala/skool-all-in-one-api). Read AND write to posts, comments, members, classroom (courses/folders/pages), files, and group settings — through a single HTTP endpoint, no browser automation.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key]'
roles: '[Content Manager]'
inputs:
- action — Supported read action plus group slug and required object identifiers.
- approved-content — User-approved action, target IDs, titles, body content, and group slug.
- member-action — Approved action, group slug, and exact memberId values returned by the actor.
outputs:
- actor-result (json)
- member-result (json)
- prefer a permanent directory)
- publication-log (markdown)
- stdout
prompts:
- List the pending members in this Skool community without approving anyone.
- Publish this approved lesson body to the named course and verify the page tree.
- Create this approved community post after showing me the final plain-text content.
- Approve these exact memberIds and return the per-member actor results.
---

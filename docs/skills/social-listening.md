---
description: Monitor online conversations to find potential customers discussing problems your product solves, then engage authentically to build trust and drive acquisition.
title: social-listening
---

# social-listening

Monitor online conversations to find potential customers discussing problems your product solves, then engage authentically to build trust and drive acquisition.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing content |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [config] |
| **Roles** | [Head of Marketing] |

Sets up social listening workflows to find and engage potential customers where they discuss problems.

## How you ask

- “Set up a Reddit monitoring plan for our product category”
- “Create a Twitter listening workflow for competitor mentions”
- “Find conversations where people discuss problems we solve”
- “Build an engagement playbook for our community presence”

## Inputs

- keywords — Terms and phrases to monitor
- platforms — Platforms to search; defaults to Reddit and HN
- icp — loaded from your vault context
- marketing-context — loaded from your vault context
- keywords — Terms to monitor
- brand_voice — Voice reference for reply drafting
- keywords — Terms to monitor on a cadence
- cadence — How often the sweep runs
- product-context — What the product does and who it serves
- subreddit — Target subreddit name
- thread — Thread URL or title + body text
- existing-replies — Current top replies for gap analysis
- tone — Optional tone guidance (technical, casual, professional)

## Outputs

- Ready-to-post reply with strategy notes and tone confidence; use the user's requested output path when supplied, otherwise the scratch location below.
- engagement-playbook (markdown)
- listening-plan (markdown)
- listening-system (markdown)
- prefer a permanent directory)
- {client.marketing}/social-listening/social-listening-{YYYY-MM-DD}.md
- {company.marketing}/social-listening/social-listening-{YYYY-MM-DD}.md


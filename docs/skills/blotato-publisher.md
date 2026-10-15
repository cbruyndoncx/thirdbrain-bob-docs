---
description: Publish and schedule posts, and generate AI visuals (images and short videos from viral templates), across many social platforms through the Blotato REST API — driven from the CLI. Covers the publish-breadth gap `social-publisher` leaves open (X/Twitter, Instagram, Threads, TikTok, Facebook, Pinterest, Bluesky) and adds the generate-then-publish loop on Blotato's credit pool.
title: blotato-publisher
---

# blotato-publisher

Publish and schedule posts, and generate AI visuals (images and short videos from viral templates), across many social platforms through the Blotato REST API — driven from the CLI. Covers the publish-breadth gap `social-publisher` leaves open (X/Twitter, Instagram, Threads, TikTok, Facebook, Pinterest, Bluesky) and adds the generate-then-publish loop on Blotato's credit pool.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing seo |
| **Level** | advanced |
| **Input** | url |
| **Output** | document |
| **Setup** | [api-key] |
| **Roles** | [Head of Marketing, Content Manager] |

Publishes/schedules posts AND generates AI visuals (images, short videos) for X/Twitter, Instagram, Threads, TikTok, Facebook, LinkedIn, YouTube, Pinterest, and Bluesky…

## How you ask

- “Publish this to X via Blotato”
- “Cross-post this to Instagram, Threads and Bluesky”
- “Schedule this TikTok for Friday 3pm”
- “Generate a quote card for this line and post it to LinkedIn”
- “Make a faceless short from this article and schedule it”
- “What accounts do I have connected in Blotato?”

## Inputs

- platform — Target platform (twitter, instagram, threads, tiktok, facebook, linkedin, youtube, pinterest, bluesky)
- account-id — Blotato accountId from the list-accounts route
- text — Post text/caption
- schedule — ISO 8601 datetime (or use next-free-slot)
- platform — Target platform
- request — Account lookup request
- file — Local image or video file
- submission-id — postSubmissionId returned by publish/schedule
- template-id — Template ID from the templates listing
- prompt — Natural-language prompt; AI auto-fills the template inputs
- type — Source type (perplexity-query, youtube, tiktok, article, pdf, audio, twitter, text)
- query — Research query or source URL/text

## Outputs

- JSON list of connected accounts
- Public URL to pass as a mediaUrl
- Publish confirmation note. Generated visuals stay Blotato-hosted URLs — download to the scratch output area (`output.scratch`) only when a local copy is needed.
- Rendered image/video URL (poll until status done)
- Resolved, sourced content (poll until completed)
- confirmation (markdown)
- conversation
- in-progress / published / failed
- prefer a permanent directory)


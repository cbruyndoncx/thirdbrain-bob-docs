---
description: 'Target Audience: YouTube creators, content marketers, and social media managers who need high-performing thumbnails without design skills or tools like Photoshop.'
title: yt-thumbnail
---

# yt-thumbnail

Target Audience: YouTube creators, content marketers, and social media managers who need high-performing thumbnails without design skills or tools like Photoshop.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | images |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [install] |
| **Roles** | [Head of Marketing, Content Manager] |

Generates high-CTR YouTube thumbnails using AI image generation and automated text/face compositing.

## How you ask

- “Generate a YouTube thumbnail for my video: How I Made $10K in 30 Days”
- “Create 5 thumbnail variants for A/B testing — title is 'Python Tips Nobody Tells You'”
- “Iterate on this thumbnail — make the text bigger and switch to the fire palette”
- “Make a thumbnail with my face photo for 'The Truth About AI in 2026'”
- “Remove the background from my profile photo for thumbnails”
- “Generate dramatic facial expressions from my headshot — amazed, excited, serious”
- “Create a gallery of all the expression variants so I can share it”

## Inputs

- title — Video title or topic for the thumbnail
- face_image — Face/person photo for compositing (PNG preferred, transparency ideal)
- style_direction — Visual direction — mood, colors, scene description
- existing_thumbnail — Path to thumbnail to improve
- feedback — What to change — text, colors, layout, background
- title — Video title
- face_image — Face photo for compositing
- face_image — Face photo (JPG or PNG) — any background
- face_image — Reference face photo (transparent PNG preferred)
- expressions — Comma-separated list of expressions to generate (default: amazed,excited,curious,serious,pointing)
- images — Glob pattern or comma-separated paths to images
- labels — Comma-separated labels for each image

## Outputs

- cutout (png)
- expression_set (png)
- gallery_image (png)
- prefer a permanent directory)
- revised_thumbnail (png)
- thumbnail (png)
- variant_set (png)
- {asset_dir}/
- {asset_dir}/{name}-nobg.png


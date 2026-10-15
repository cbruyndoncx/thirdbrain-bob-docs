---
description: Generate lip-synced talking head videos through a backend router — MuseTalk (local GPU-based, default) or HeyGen (cloud-hosted, no GPU needed). Includes video dubbing into 175+ languages via HeyGen's video-translate.
title: avatar-video
---

# avatar-video

Generate lip-synced talking head videos through a backend router — MuseTalk (local GPU-based, default) or HeyGen (cloud-hosted, no GPU needed). Includes video dubbing into 175+ languages via HeyGen's video-translate.

- **Area:** Marketing
- **Category:** video
- **Level:** expert
- **Input:** conversation
- **Output:** video-script
- **Setup:** api-key, install
- **Roles:** Head of Marketing, Content Manager

Generates lip-synced talking head videos with MuseTalk (local) or HeyGen (cloud), with optional Remotion compositing.

## How you ask

- “Create a talking head video from this photo and script”
- “Generate a lip-synced avatar for our product demo”
- “Make a spokesperson video using MuseTalk from this image”

## Inputs

- source (Simple avatar) — Script or message text
- backend — Backend choice: musetalk (default, requires GPU) | heygen (cloud, requires HEYGEN_API_KEY) (musetalk | heygen)
- avatar-id — HeyGen avatar ID (if using heygen backend and reusing existing avatar)
- source (Narrated slides) — Slides JSON + narration pairs
- source (Composited video) — Script text (will run generate route first, then composite)
- video-path — Path to or URL of video to translate
- target-languages — Target language(s): e.g. ['es', 'fr', 'ja'] — full list via `heygen video-translate languages list`

## Outputs

- avatar-video (video)
- composited-video (video)
- dubbed-video (video)
- dubbing-log (json)
- narrated-video (video)


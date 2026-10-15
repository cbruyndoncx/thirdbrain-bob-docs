---
description: Process videos using ffmpeg - compress, trim, scale, extract audio, convert formats.
title: process-video
---

# process-video

Process videos using ffmpeg - compress, trim, scale, extract audio, convert formats.

- **Area:** Marketing
- **Category:** video
- **Level:** advanced
- **Input:** conversation
- **Output:** video-script
- **Setup:** install
- **Roles:** 

## How you ask

- “Compress this video file for YouTube upload”
- “Trim this screen recording to remove the first 30 seconds”
- “Extract the audio track from this video”
- “Scale this 4K video down to 1080p for web”

## Inputs

- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- Processed video for a marketing project (company or client scope)
- compressed-mp4 (video)
- extracted-audio (audio)
- prefer a permanent directory)
- scaled-mp4 (video)
- trimmed-mp4 (video)
- {scope.marketing}/videos/process-video-{YYYY-MM-DD}.mp4


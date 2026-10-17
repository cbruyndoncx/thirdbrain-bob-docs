---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: process-video — ThirdBrain BOB skill
  description: Process videos using ffmpeg - compress, trim, scale, extract audio, convert formats.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: process-video
catLabel: video
area: marketing
desc: Process videos using ffmpeg - compress, trim, scale, extract audio, convert formats.
summary: Process videos using ffmpeg - compress, trim, scale, extract audio, convert formats.
difficulty: advanced
inputType: conversation
outputType: video-script
requires: '[install]'
roles: '[]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- Processed video for a marketing project (company or client scope)
- compressed-mp4 (video)
- extracted-audio (audio)
- prefer a permanent directory)
- scaled-mp4 (video)
- trimmed-mp4 (video)
- '{scope.marketing}/videos/process-video-{YYYY-MM-DD}.mp4'
prompts:
- Compress this video file for YouTube upload
- Trim this screen recording to remove the first 30 seconds
- Extract the audio track from this video
- Scale this 4K video down to 1080p for web
---

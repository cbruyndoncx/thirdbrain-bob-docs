---
description: 'Target Audience: Marketers, content creators, and business owners producing social video ads, B-roll, LinkedIn shorts, or product demos without a film crew.'
title: veo-video-gen
---

# veo-video-gen

Target Audience: Marketers, content creators, and business owners producing social video ads, B-roll, LinkedIn shorts, or product demos without a film crew.

- **Area:** Marketing
- **Category:** video
- **Level:** advanced
- **Input:** conversation
- **Output:** video-script
- **Setup:** api-key
- **Roles:** Head of Marketing, Content Manager

Generate AI videos using Google Veo 3.1 via Gemini API directly (no inference.sh dependency).

## How you ask

- “Gemini video”
- “UGC ad”
- “LinkedIn video short”

## Inputs

- prompt — Prompt used to generate a video from a text prompt only
- aspect_ratio — Aspect ratio used to generate a video from a text prompt only (969 | 556)
- prompt — Prompt used to animate a start image, optionally interpolating to an end image
- image — Start frame (first frame of output)
- end_image — End frame for interpolation — must be visually similar to start image
- video_prompt — Video prompt used to veo video with separate OpenAI TTS narration merged via FFmpeg
- voice_script — Voice script used to veo video with separate OpenAI TTS narration merged via FFmpeg
- voice — Voice used to veo video with separate OpenAI TTS narration merged via FFmpeg (alloy | echo | fable | onyx | nova | shimmer)

## Outputs

- generated-video (mp4)
- prefer a permanent directory)


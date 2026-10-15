---
description: 'Turn any source video into a commentary / reaction / video-essay MP4 that runs fully headless: AI selects the segments worth commenting on, edge-tts narrates the commentary, ASS renders on-screen captions and commentary cards, and ffmpeg stitches it into one 16:9 video — with an attribution block that links back to the original.'
title: commentary-video
---

# commentary-video

Turn any source video into a commentary / reaction / video-essay MP4 that runs fully headless: AI selects the segments worth commenting on, edge-tts narrates the commentary, ASS renders on-screen captions and commentary cards, and ffmpeg stitches it into one 16:9 video — with an attribution block that links back to the original.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** install
- **Roles:** Head of Marketing, Content Manager

Generates a headless commentary/reaction video from a source video — AI-cuts the segments worth reacting to, narrates the commentary with edge-tts, burns on-screen…

## How you ask

- “Make a commentary video reacting to this YouTube video: {url}, arguing that isolated project memory doesn't compound”
- “Cut this talk down to the key claims and add my talk-over commentary”
- “Do a silent text-only video essay on this video”
- “React to this video — clip the hot takes and comment on each”
- “Turn this into a reaction video and link back to the original in the description”

## Inputs

- source_url_or_video — YouTube/social URL, or a local MP4 path already on disk
- commentary_angle — The POV that steers segment selection (e.g. 'he abandoned the custom brain — here's why structured beats conversational memory')
- source_url_or_video — YouTube/social URL, or a local MP4 path
- commentary_angle — The steering POV for segment selection

## Outputs

- Final MP4, beside {name}_description.md and {name}_script.md. Moving it into a marketing folder is a deliberate, human-confirmed step and never the default.
- description (markdown)
- prefer a permanent directory)


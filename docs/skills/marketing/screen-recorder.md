---
description: Two deterministic scripts that make a raw screen capture of an agent session useful without anyone watching it end to end. Both are consumed by other skills and playbooks (demo-video, process-video, session-recording playbooks), which is why they live here and not inside one of them.
title: screen-recorder
---

# screen-recorder

Two deterministic scripts that make a raw screen capture of an agent session useful without anyone watching it end to end. Both are consumed by other skills and playbooks (demo-video, process-video, session-recording playbooks), which is why they live here and not inside one of them.

- **Area:** Marketing
- **Category:** video
- **Level:** expert
- **Input:** conversation
- **Output:** video-script
- **Setup:** api-key, install
- **Roles:** 

Turns raw screen recordings of agent sessions into usable artefacts — cuts idle time out of a capture using the session log as the timeline, and converts a recording…

## How you ask

- “Cut the dead air out of yesterday's demo recording using the session log”
- “Which log window matches this 950-second video?”
- “Turn this screen recording into an SOP with timestamps”

## Inputs

- log — Exported agent client log with one timestamped heading per message
- video — Raw screen recording
- video_start — Wall-clock time the recording began, HH:MM:SS (from the capture filename)
- video — Local screen recording with narration

## Outputs

- highlight (mp4)
- prefer a permanent directory)
- sop (markdown)


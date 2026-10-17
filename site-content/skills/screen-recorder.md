---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: screen-recorder — ThirdBrain BOB skill
  description: Two deterministic scripts that make a raw screen capture of an agent session useful without anyone watching it end to end. Both are consumed by other skills and
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: screen-recorder
catLabel: video
area: marketing
desc: Turns raw screen recordings of agent sessions into usable artefacts — cuts idle time out of a capture using the session log as the timeline, and converts a recording…
summary: Two deterministic scripts that make a raw screen capture of an agent session useful without anyone watching it end to end. Both are consumed by other skills and playbooks (demo-video, process-video, session-recording playbooks), which is why they live here and not inside one of them.
difficulty: expert
inputType: conversation
outputType: video-script
requires: '[api-key, install]'
roles: '[]'
inputs:
- log — Exported agent client log with one timestamped heading per message
- video — Raw screen recording
- video_start — Wall-clock time the recording began, HH:MM:SS (from the capture filename)
- video — Local screen recording with narration
outputs:
- highlight (mp4)
- prefer a permanent directory)
- sop (markdown)
prompts:
- Cut the dead air out of yesterday's demo recording using the session log
- Which log window matches this 950-second video?
- Turn this screen recording into an SOP with timestamps
---

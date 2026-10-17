---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: yt-script-structure — ThirdBrain BOB skill
  description: Build retention-optimized video script outlines and write full spoken-word scripts for YouTube. Script structure is the single biggest lever for audience retent
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: yt-script-structure
catLabel: content
area: marketing
desc: Structure and write YouTube video scripts with retention-optimized frameworks.
summary: Build retention-optimized video script outlines and write full spoken-word scripts for YouTube. Script structure is the single biggest lever for audience retention -- not editing, not production value, not B-roll. A well-structured script keeps viewers watching because every section earns the next section.
difficulty: beginner
inputType: conversation
outputType: code
requires: '[none]'
roles: '[Content Manager]'
inputs:
- topic — Core video idea in one sentence
- title — Video title the script must deliver on
- target_length — Target video length (default 8-12 min)
- format — Talking head, screen share, hybrid, story-driven (talking-head | screen-share | hybrid | story-driven)
- key_points — 3-5 key points to cover
- outline — Existing script outline (from structure route or manual)
- topic — Core video idea
- title — Video title
- target_length — Target video length
outputs:
- Full spoken-word script with visual directions, retention beats, and timing
- Structured outline with framework, sections, retention beats, and timing
- '{company.marketing}/video/scripts/{video-slug}_script_{YYYY-MM-DD}.md'
prompts:
- Write a script
- Script my video
- Outline a video
---

---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Daily Content Machine
  description: Daily Content Machine — how BOB researches & scripts a video before you record
  socialImage: https://img.youtube.com/vi/zNGSZ9FA9pQ/maxresdefault.jpg
skillName: pb-daily-content-machine
youtubeId: zNGSZ9FA9pQ
published: '2026-06-29'
privacy: public
title: Daily Content Machine — how BOB researches & scripts a video before you record
thumbnail: https://img.youtube.com/vi/zNGSZ9FA9pQ/maxresdefault.jpg
subtitle: A morning content brief (top trend angle + full script + 3 thumbnail concepts) delivered daily and unattended, stopping at the point where you record
inputs:
- label: youtube-context.md
  icon: 🎯
- label: tone_of_voice.md
  icon: 🗣️
- label: content-trends domain
  icon: 📡
outputs:
- label: scored-outliers.md
  icon: 📊
- label: angle+hooks.md
  icon: 💡
- label: script.md
  icon: 📝
- label: thumb-1..3.png
  icon: 🖼️
- label: content-brief.md
  icon: 📋
steps:
- label: continuous-research → scout & score trend outliers
  actor: agent
- label: yt-idea-generation → pick top angle + 5 hooks
  actor: agent
- label: yt-script-structure → full script in brand voice
  actor: agent
- label: yt-hook-writing → craft & prepend the hook
  actor: agent
- label: yt-thumbnail → 3 on-brand thumbnail concepts
  actor: agent
- label: daily-briefing → assemble the morning brief
  actor: agent
- label: You record the video
  actor: human
trigger: '"Every morning — today''s best content opportunity, scripted and thumbnailed"'
timeSavings: ~2 hrs trend-hunting + scripting → 10-20 min unattended
compounding: Each day's brief sharpens your trend signal and voice templates
frequency: Daily, unattended (06:00)
hook: 'Every morning, the same question.

  What should I post today?'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: marketing
---

An autonomous morning pipeline: scout trending outliers, pick the angle, write the script in your voice, generate thumbnail concepts, deliver a ready-to-record brief — stopping at the one human step: you record.

More at brn.cx

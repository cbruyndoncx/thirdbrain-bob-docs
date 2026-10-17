---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: talk-to-me — ThirdBrain BOB skill
  description: Speak the answer instead of printing it, when reading the screen is the problem.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: talk-to-me
catLabel: productivity
area: foundational
desc: Reads answers aloud through the computer's speakers instead of writing them to the screen.
summary: Speak the answer instead of printing it, when reading the screen is the problem.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder]'
inputs:
- text — What to say. Rewritten for the ear before synthesis, not read verbatim.
- voice — Neural voice name, e.g. en-GB-SoniaNeural. Defaults to the British female voice.
- content — The material to brief on — a task list, a decision set, a status summary
- batches — How many batches to split into. Defaults to one per natural grouping, 3-5 items each.
- trigger — No input needed; run when audio fails or on a new machine
- state — Whether to start or stop speaking answers by default (True | False)
outputs:
- console
- mode-acknowledgement (text)
- played in sequence, one Bash call per batch
- played through the platform's audio player; the mp3 is deleted after playback
- setup-report (text)
- spoken-audio (audio)
- spoken-briefing (audio)
prompts:
- Talk to me — I can't read my screen right now
- Read that summary out loud
- Give me the briefing in audio, in batches so I can stop you
- Stop speaking, back to text
---

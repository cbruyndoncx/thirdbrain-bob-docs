---
description: Speak the answer instead of printing it, when reading the screen is the problem.
title: talk-to-me
---

# talk-to-me

Speak the answer instead of printing it, when reading the screen is the problem.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | productivity |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder] |

Reads answers aloud through the computer's speakers instead of writing them to the screen.

## How you ask

- “Talk to me — I can't read my screen right now”
- “Read that summary out loud”
- “Give me the briefing in audio, in batches so I can stop you”
- “Stop speaking, back to text”

## Inputs

- text — What to say. Rewritten for the ear before synthesis, not read verbatim.
- voice — Neural voice name, e.g. en-GB-SoniaNeural. Defaults to the British female voice.
- content — The material to brief on — a task list, a decision set, a status summary
- batches — How many batches to split into. Defaults to one per natural grouping, 3-5 items each.
- trigger — No input needed; run when audio fails or on a new machine
- state — Whether to start or stop speaking answers by default (True | False)

## Outputs

- console
- mode-acknowledgement (text)
- played in sequence, one Bash call per batch
- played through the platform's audio player; the mp3 is deleted after playback
- setup-report (text)
- spoken-audio (audio)
- spoken-briefing (audio)


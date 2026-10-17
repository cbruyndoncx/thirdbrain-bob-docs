---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: humanize-content — ThirdBrain BOB skill
  description: Transform AI-generated drafts into authentic-sounding text by removing detectable AI patterns, injecting real voice, and adding personal specificity. The method
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: humanize-content
catLabel: documents
area: foundational
desc: Transforms AI-generated text to sound authentically human.
summary: 'Transform AI-generated drafts into authentic-sounding text by removing detectable AI patterns, injecting real voice, and adding personal specificity. The method applies five sequential passes: pattern purge, voice injection, specificity anchoring, structural variation, and read-aloud refinement.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- text — AI-generated text to humanize (paste or file path)
- tone-hint — Voice register to write toward when no voice profile is on file. Skill-local — it steers Pass 2 only and is not written to any entity field. (casual | professional | technical)
- pass-depth — How much of the 5-pass framework to run. Defaults to the full sequence; the reduced setting stops after Pass 1 and is the mandatory setting under 150 words, where Passes 3-5 add more placeholders than prose. Skill-local. (full | pattern-purge-only)
- text — AI-generated text to humanize
- writing-samples — Optional 3-5 existing writing samples for voice extraction
- scope — Whether the profile is the operator's own voice or the company's. The choice decides which profile path the file lands in and which voice later runs load. (personal | company)
- writing-samples — Optional 3-5 writing samples for voice extraction
outputs:
- Persistent voice DNA loaded silently by later runs. The `scope` input picks which of the two paths it lands in.
- 'Rewritten text with the change log and the before/after comparison, plus any `[YOUR: ...]` placeholders the user must fill.'
- Run-scoped voice DNA built from the interview or samples. Temporary — promote it via `voice-setup` to make it persistent.
- Voice-anchored rewrite with the per-pass change log and the before/after comparison.
- prefer a permanent directory)
- '{me.profile-root}/humanize-voice-profile.md'
prompts:
- Humanize this
- Make this sound less AI
- This sounds robotic
---

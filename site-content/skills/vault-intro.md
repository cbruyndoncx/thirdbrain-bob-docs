---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: vault-intro — ThirdBrain BOB skill
  description: A 5-module hands-on tutorial for new users. Works inside Claude Code alongside Obsidian. Each module ends with Claude creating a real file in the vault so the u
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: vault-intro
catLabel: utilities
area: foundational
desc: Interactive onboarding tutorial for new vault users.
summary: A 5-module hands-on tutorial for new users. Works inside Claude Code alongside Obsidian. Each module ends with Claude creating a real file in the vault so the user can watch it appear in Obsidian in real-time.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- experience_level — How much the learner already knows — new-to-obsidian, new-to-this-vault, or returning. Sets which modules run and how much Obsidian basics to cover. (new-to-obsidian | new-to-this-vault | returning)
- module — Module number to jump to (0-5)
- current_module — Module just completed; inferred from session state when omitted
- module — Module to recap; defaults to the one just completed
- question — The learner's off-topic question
- current_module — Where to resume the tutorial afterwards
outputs:
- Personalised starter kit written at the end of Module 5 only — five role-matched essential skills and a quick reference. A permanent note in the owner's root, not scratch.
- prefer a permanent directory)
- tutorial-progress (markdown)
- tutorial-recap (markdown)
- '{me.root}/vault_intro_starter_kit.md'
prompts:
- I'm new to Obsidian — show me how to use this vault
- /vault-intro start
- /vault-intro module-2
- /vault-intro next
- Take me through the tutorial from the beginning
- I've used Obsidian before but I'm new to the vault — skip to module 2
---

---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: macrodeck-config — ThirdBrain BOB skill
  description: Configures [Macro Deck](https://macro-deck.app) ([source](https://github.com/Macro-Deck-App/Macro-Deck)) by reading and writing its on-disk config directly, rat
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: macrodeck-config
catLabel: utilities
area: foundational
desc: Reads and edits Macro Deck (open-source Stream Deck alternative, macro-deck.app) button profiles by manipulating its on-disk config directly — profiles.db, config.json,…
summary: Configures [Macro Deck](https://macro-deck.app) ([source](https://github.com/Macro-Deck-App/Macro-Deck)) by reading and writing its on-disk config directly, rather than clicking through the GUI. Macro Deck stores profiles (button layouts) as a JSON blob inside a SQLite database — this skill knows that schema, the JSON contract each installed plugin's actions use, and the safe read-close-write-reopen pattern needed to avoid corrupting a live config.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- appdata_path — Path to the Macro Deck user directory (default `%AppData%\Macro Deck` via /mnt/c/Users/<user>/AppData/Roaming/Macro Deck)
- button_specs — Desired buttons — label, action(s), grid position, optional status binding
- plugin_repo_url — Plugin repo url used to clone a plugin's source to /tmp/repos and extract its Actions/*.cs $type + Configuration shape when the format is unknown
outputs:
- action-catalog-entry (markdown)
- config-summary (markdown)
- mutation-script (python)
- user-specified output path for action catalog entry
- user-specified output path for config summary
- '{output.scripts}/macrodeck_add_buttons_{date}.py'
prompts:
- Configure Macro Deck
- Add a button to my macro deck
- Macro deck hotkey
---

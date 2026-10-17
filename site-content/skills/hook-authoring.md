---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: hook-authoring — ThirdBrain BOB skill
  description: Keeps hook configurations equivalent and maintainable across Claude Code, OpenAI Codex CLI, the Antigravity CLI (`agy`), Google Gemini CLI, and Goose. Authors n
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: hook-authoring
catLabel: utilities
area: foundational
desc: Authors and maintains equivalent hook configs across Claude Code, Codex, Antigravity CLI, Gemini CLI, and Goose.
summary: Keeps hook configurations equivalent and maintainable across Claude Code, OpenAI Codex CLI, the Antigravity CLI (`agy`), Google Gemini CLI, and Goose. Authors new hooks from a single description, migrates between platforms, audits parity, and validates config syntax.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- event — Hook event (PreToolUse, PostToolUse, SessionStart, Stop)
- matcher — Regex matcher for the tool name or command
- command — Shell command to execute
- platforms — Target platforms (default Claude Code, Codex and Antigravity; Gemini CLI and Goose on request)
- vault_root — Path to vault root (defaults to current directory)
- source_path — Path to the source config file
- target_platform — Target platform (claude-code, codex, antigravity, gemini-cli, goose)
- 'config_path — Path to the config file to validate. validate-hooks.sh accepts no path argument: run it from the project root for its fixed Claude, Codex and Antigravity paths. Validate other paths and Gemini CLI or Goose configurations manually against the platform reference.'
outputs:
- .claude/settings.json, .codex/hooks.json, .agents/hooks.json, .gemini/settings.json, .agents/plugins/*/hooks/hooks.json
- Config snippet for the target platform, with migration notes for unsupported features
- Hooks present on one platform but missing on others, with fix commands
- Syntax check results, schema compliance, and common error fixes
- conversation
- hook-configs (json/toml)
- user-specified output path for migrated config
prompts:
- Add a hook
- Keep hooks in sync
- Migrate hooks to Codex
---

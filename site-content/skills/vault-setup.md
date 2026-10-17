---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: vault-setup — ThirdBrain BOB skill
  description: 'Target audience: anyone standing up a fresh vault, taking one over, or rebranding an existing one — and anyone who needs to change a single identity field witho'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: vault-setup
catLabel: obsidian
area: foundational
desc: Personalises a vault's identity — owner name, company name and entity id, vault display name, and published-site domain — with a guided interview, a preview of every…
summary: 'Target audience: anyone standing up a fresh vault, taking one over, or rebranding an existing one — and anyone who needs to change a single identity field without re-answering everything.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- vault — Vault root to configure; defaults to the current vault
- section — One of owner, company, vault-identity, context-pack
- vault — Vault root to inspect; defaults to the current vault
outputs:
- AGENTS.md
- CLAUDE.md
- Canonical agent bootstrap contract at vault root — holds the vault display name heading and the metalsmith site-domain row
- Claude pointer at vault root; rewritten only while it still carries the full contract (older vaults), otherwise 0 occurrences
- Company identity written by the company section
- Files covered by the named section — owner writes `me.profile`, company writes `company.profile`, vault-identity writes AGENTS.md (and CLAUDE.md where it still holds the full contract) and, with --from-vault, rewrites matching obsidian:// vault references and OBSIDIAN_VAULT assignments in supported text files outside excluded directories
- Owner identity written by the owner section
- Scaffolded by the context-pack section on a vault that has no pack yet; file locations and filing conventions are edited there, never into profile prose
- current-values (json)
- stdout
- '{company.profile}'
- '{me.profile}'
- '{section-owned-context-file}'
- '{skills.root}/context-{company-id}/context.yaml'
prompts:
- Set up this vault for a new company
- We're rebranding — change the company name everywhere
- vault-setup owner
- What owner and company is this vault currently configured for?
---

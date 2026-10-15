---
title: Skills over MCP — Local and Served Skills
---

# Skills over MCP — Local and Served Skills

A BOB vault reaches its skills, playbooks and value chains in one of two ways. Agents and people
should recognise both.

| | Full vault | Starter vault |
|---|---|---|
| Skills | All local, in `{skills.root}` (default `00-CORE/Agents/skills/`) | Only the skills that operate the vault are local; every other skill is served by the skills MCP server |
| Playbooks | Local, in `00-CORE/Playbooks/` | Served by the skills MCP server |
| Value chains | Local, in `VALUE-CHAINS.md` | Served by the skills MCP server |
| Catalogues | [SKILLS](../skills/index.md), [PLAYBOOKS](../03-Learn/Concepts/playbooks.md), VALUE-CHAINS | Ask the MCP server; the local catalogues are absent or list only the local skills |

Both variants use the same workspace: the same folders, data model, templates, Bases, TaskNotes,
BOB Workspace and agent hooks. Notes a served skill writes are routed and validated exactly like
notes a local skill writes.

## The local skills in a starter vault

These run the vault itself and are always local, because the agent hooks, the BOB Workspace plugin
and the templates call them by path:

`context-pack`, `vault-validator`, `tasknotes`, `personal-backlog`, `obsidian-ops`,
`bob-workspace-bootstrap`, `bob-workspace-compose`, `bob-install`, `bob-doctor`, `acp-doctor`,
`obsidian-plugin-manager`, `vault-setup`, `vault-upgrade`, `vault-preflight`.

## Finding a skill, playbook or value chain

1. **Local first.** If `{skills.root}/<name>/SKILL.md` exists, use it.
2. **Otherwise ask the skills MCP server.** Its tools share one prefix: the server's `--prefix`, or
   the library namespace (`bob_`) when it serves one library. Use `…_search_skills` or
   `…_list_skills` to find a skill, `…_get_skill` to read its `SKILL.md`, and
   `…_read_skill_file` for its references. Use `…_list_playbooks` / `…_get_playbook` for
   playbooks and `…_list_value_chains` / `…_get_value_chain` for value chains. Playbooks are also
   offered as MCP prompts.
3. A skill can appear in both places, for example `tasknotes`. Both are the same skill; the local
   copy is the one installed with this vault.

A playbook step that names a skill works the same way: run it locally if the skill is local,
otherwise fetch it from the MCP server.

## Running a served skill's scripts

Reading a served skill needs nothing else. To run its scripts, copy it to disk together with the
skills it declares as runtime dependencies, then run the commands from the skill folder as usual
and hand them the vault:

```bash
npx github:cbruyndoncx/ThirdBrain-skills-mcp pull <skill> --with-deps \
  --command <the server command below> --to ~/.cache/skills-mcp-client/bob
cd ~/.cache/skills-mcp-client/bob/<skill>
VAULT_PATH=<vault> uv run scripts/<script>.py --vault <vault>
```

`--with-deps` pulls the whole dependency closure, so approve it as one unit. `--sync` on a later
pull fetches only what changed.

## API keys for served skills

A served skill runs outside the vault, so it does not read the vault's `.env`. Ask your AI coder to
set the keys that skill needs in your environment. Where they go depends on your MCP host: your
shell profile, the host's own settings, or the `env` of its MCP server configuration.
`.env.example` in the vault root lists the keys and the skills that use them.

## Connecting the skills MCP server

Register the server once per machine. For Claude Code:

```bash
claude mcp add --scope user skills -- npx github:cbruyndoncx/ThirdBrain-skills-mcp \
  --lib bob=<skills pack> --exclude-tiers internal,private --dev-status integrated
```

`<skills pack>` is the BOB skills pack: a downloaded `.zip`, or an `https://…zip#sha256=<digest>`
URL pinned to its checksum. The library ZIP is in the Skool community; download it there and check it against its
`.sha256` file. A full vault can also serve itself, with `--lib bob=<vault>`.

Check the connection with `claude mcp get skills`. The first call after a restart can take a while,
because the server scans the whole library before it answers.

## Related

- [symlink_setup](symlink_setup.md): how the AI tools find the local skills
- AGENTS: the bootstrap contract, including how skill commands are run

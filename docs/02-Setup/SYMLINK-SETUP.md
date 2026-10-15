---
description: 'Canonical link-type reference: junction vs symlink per filesystem, reparse
  tags, Windows-side verification. Moved from 00-CORE/Agents/ 2026-09-01.'
title: Symlink Setup for Cross-Platform Skills — canonical reference
---

# Symlink Setup for Cross-Platform Skills

> **Folder names below are the default (numbered) layout that BOB ships with.** A workspace
> with its own context pack names the folders differently — `uv run 00-CORE/Agents/skills/context-pack/scripts/resolve_context.py --key skills.root`
> prints the real path for the key named in each case.

This guide shows how to create symlinks to `00-CORE/Agents/skills/` for multiple AI assistants (Claude, Gemini, Codex).

## Why Symlink?

- **Single Source of Truth**: All AI assistants read from `00-CORE/Agents/skills/`
- **Platform Compatibility**: Each AI expects skills in its own directory (`.claude/skills/`, `.gemini/skills/`, `.codex/skills/`)
- **No Duplication**: Update once, available everywhere

## Which link type do I need?

Start here — most platforms need nothing special.

| Host OS | Vault filesystem | Use | Notes |
|---|---|---|---|
| **macOS** | APFS / HFS+ | `ln -s` | Native POSIX symlinks. Cowork is a native Mac app on the same filesystem — nothing extra needed. |
| **Linux** (any distro) | ext4 / btrfs / xfs / zfs | `ln -s` | Same. Distro is irrelevant — this is kernel VFS behaviour, identical on Ubuntu, Fedora, Arch, NixOS. |
| **Windows only** (no WSL) | NTFS | `mklink /J` | Junction. |
| **WSL + any Windows client** | NTFS | `mklink /J` | ⚠️ **The only problem case.** See below. |

**Junctions are an NTFS feature. They do not exist on macOS or Linux, and are not needed there** —
`mklink` is a Windows `cmd` builtin with no POSIX equivalent. On a Unix filesystem there is exactly
one symlink implementation and every process resolves it identically, so `ln -s` is complete and
correct.

The Windows trouble is not "symlinks are fragile". It is that WSL and Win32 are **two operating
systems sharing one filesystem** and disagreeing about how a link is stored. That disagreement can
only happen on NTFS.

### Other filesystem gotchas (all platforms)

- **exFAT / FAT32** (USB drives, SD cards): no symlink support at all. `ln -s` fails outright. Keep
  the vault on a native filesystem.
- **Cloud-sync folders** (Dropbox, iCloud Drive, OneDrive, Google Drive): most sync clients do not
  preserve symlinks — they either dereference them into full copies or drop them. This silently
  duplicates the entire skill tree or breaks the link on the second machine. Do not put the vault
  inside a sync folder.
- **Network shares** (SMB/NFS): symlink support depends on server config and mount options. Verify
  with the child-count check below before trusting it.

## Requirement: Windows-resolvable links (Claude Cowork, Obsidian, any native tool)

> **Windows hosts only.** On macOS and Linux, `ln -s` is correct — skip this section.
>
> **If you want to run Claude Cowork on a Windows vault, the links must be Windows-native junctions,
> not WSL symlinks.** This is a hard requirement, not a preference.

A symlink created from WSL with `ln -s` is stored as reparse tag `0xA000001D`
(`IO_REPARSE_TAG_LX_SYMLINK`). **Only WSL can follow it.** The Win32 API returns an empty
`LinkType`, an empty `Target`, and **zero children** — so any Windows-native process sees
`.claude/skills/` as an *empty directory*.

This fails **silently**. There is no error, no warning, no broken-link message: the skill list is
simply empty, which is indistinguishable from "this vault has no skills". Same for `.claude/agents`
(subagents), `.gemini/skills`, and `.codex/skills`.

| Link created from | WSL CLI | Claude Cowork / Windows-native |
|---|---|---|
| WSL `ln -s` | ✅ resolves | ❌ **0 skills, no error** |
| Windows junction (`mklink /J`) | ✅ resolves | ✅ resolves |
| Windows symlink (`mklink /D`) | ✅ resolves | ✅ resolves (needs admin/Developer Mode) |

**Use a junction.** It is the only method that needs no elevation and works from both sides.

### Verify which kind you have

```powershell
fsutil reparsepoint query .claude\skills
(Get-ChildItem .claude\skills -Force).Count
```

Tag `0xA000001D` or a child count of `0` means the link is WSL-only and Cowork will see nothing.
`ls` from WSL or Git Bash will look fine either way — **it is not a valid check.** Only the Windows
child count is.

**macOS / Linux equivalent** — one command, and a non-zero count is conclusive:

```bash
ls .claude/skills/ | wc -l    # must be > 0
readlink .claude/skills       # shows the target
```

There is no second filesystem view to cross-check on these platforms; if the count is right, every
client will see the same thing.

### Fix (no admin required)

```bat
rmdir .claude\skills & rmdir .claude\agents & rmdir .gemini\skills & rmdir .codex\skills
mklink /J .claude\skills 00-CORE\Agents\skills
mklink /J .claude\agents 00-CORE\Agents\subagents
mklink /J .gemini\skills 00-CORE\Agents\skills
mklink /J .codex\skills 00-CORE\Agents\skills
```

`rmdir` on a reparse point deletes the link only — it never touches the target. Restart the client
afterward so skill discovery re-runs.

**Tradeoff**: junctions store an *absolute* target, so moving or renaming the vault breaks them
(re-run the block above). Relative WSL symlinks survive a move but are invisible to Windows. Pick
portability or Cowork compatibility — you cannot have both from a single link.

## Setup Instructions

### Linux / macOS / WSL

> ✅ **macOS and Linux: this is the correct and only method.** Works for Claude Code, Claude Cowork,
> Obsidian, and every CLI. Nothing further is required — the junction section above does not apply
> to you.
>
> ⚠️ **WSL on an NTFS vault (`/mnt/c`, `/mnt/d`): do not use this.** Links made here carry reparse
> tag `0xA000001D` and are invisible to every Windows-native tool, including Cowork. Use the
> junction recipe above instead. (Safe if the vault lives inside the WSL filesystem itself, e.g.
> `~/vault` on ext4 — but then Windows tools cannot use the vault at all.)

```bash
# From vault root directory
cd /path/to/your/vault

# Create directories first
mkdir -p .claude .gemini .codex

# Create symlinks for all platforms (using $(pwd) for dynamic path)
ln -s $(pwd)/00-CORE/Agents/skills .claude/skills
ln -s $(pwd)/00-CORE/Agents/skills .gemini/skills
ln -s $(pwd)/00-CORE/Agents/skills .codex/skills
```

Verify:
```bash
ls -la .claude/ .gemini/ .codex/
# Should show: skills -> /path/to/your/vault/00-CORE/Agents/skills (in each)
```

### Windows (Command Prompt)

**Run as Administrator**:

```cmd
cd C:\path\to\your\vault

REM Create directories
mkdir .claude .gemini .codex

REM Create symlinks for all platforms (relative paths work here)
mklink /D ".claude\skills" "00-CORE\Agents\skills"
mklink /D ".gemini\skills" "00-CORE\Agents\skills"
mklink /D ".codex\skills" "00-CORE\Agents\skills"
```

### Windows (PowerShell)

**Run as Administrator**:

```powershell
cd C:\path\to\your\vault

# Create directories
New-Item -ItemType Directory -Force -Path .claude, .gemini, .codex

# Create symlinks for all platforms (relative paths work here)
New-Item -ItemType SymbolicLink -Path ".claude\skills" -Target "00-CORE\Agents\skills"
New-Item -ItemType SymbolicLink -Path ".gemini\skills" -Target "00-CORE\Agents\skills"
New-Item -ItemType SymbolicLink -Path ".codex\skills" -Target "00-CORE\Agents\skills"
```

### Verification

After creating the symlink:

1. **Check the link**:
   ```bash
   ls -la .claude/
   ```
   Should show `skills -> 00-CORE/Agents/skills`

2. **Verify access**:
   ```bash
   ls .claude/skills/
   ```
   Should show the same content as `00-CORE/Agents/skills/`

3. **Restart Claude Code**:
   - Exit and restart Claude Code
   - Ask: "What skills are available?"
   - Your skills from `00-CORE/Agents/skills/` should appear

## Troubleshooting

### Permission Denied (Windows)
- Run Command Prompt or PowerShell as Administrator
- Right-click → "Run as administrator"

### Symlink Not Working
- Check if Developer Mode is enabled (Windows 10+):
  - Settings → Update & Security → For developers → Developer Mode

### Skill list is empty, but no error (Claude Cowork / Obsidian / any Windows client)
The classic symptom of a WSL symlink read by a Windows process. `ls -la` from WSL or Git Bash shows
a healthy `lrwxrwxrwx` link and lists every skill, so the link *looks* fine — but Windows resolves
nothing and reports an empty directory rather than a failure.

Confirm and fix:

```powershell
fsutil reparsepoint query .claude\skills      # 0xA000001D = WSL-only
(Get-ChildItem .claude\skills -Force).Count   # 0 = Windows sees nothing
```

Then apply the junction fix in the requirement section at the top. Restart the client afterward.

**Do not diagnose this from WSL.** A passing `ls` there proves nothing about the Windows side.

### Wrong Path
- Use absolute paths for reliability
- Windows: `C:\Users\...` or `D:\OBS\...`
- WSL: `/mnt/d/OBS/...`
- Linux/Mac: `/home/user/...`

### Already Exists Error
```bash
# Remove existing directory/link first
rm -rf .claude/skills
# Then create symlink
ln -s /full/path/to/00-CORE/Agents/skills .claude/skills
```

## Alternative: Relative Symlink

If you want a portable setup (relative path):

```bash
cd .claude
ln -s ../00-CORE/Agents/skills skills
```

This works as long as the relative structure stays the same.

## Testing the Setup

1. **Check symlink**:
   ```bash
   ls -la .claude/skills
   ```

2. **List skills**:
   ```bash
   ls .claude/skills/
   ```
   Should show: `business-baseline/` and other skills

3. **Read a skill**:
   ```bash
   cat .claude/skills/business-baseline/SKILL.md
   ```
   Should display the skill content

4. **Restart Claude Code** and verify skills load

## Current Setup

This vault has these links in place:
- `.claude/skills` → `00-CORE/Agents/skills` (Claude Code)
- `.claude/agents` → `00-CORE/Agents/subagents` (subagents)
- `.gemini/skills` → `00-CORE/Agents/skills` (Gemini)
- `.codex/skills` → `00-CORE/Agents/skills` (Codex CLI)
- Universal skills in `00-CORE/Agents/skills/`

> **Status — 2026-08-12: all four converted to Windows junctions (tag `0xA0000003`,
> `IO_REPARSE_TAG_MOUNT_POINT`). Verified resolving from both sides.** This vault is now
> Cowork-compatible.
>
> | Link | Windows children | POSIX children |
> |---|---|---|
> | `.claude/skills` | 400 | 399 |
> | `.claude/agents` | 4 | 4 |
> | `.gemini/skills` | 400 | 399 |
> | `.codex/skills` | 400 | 399 |
>
> 390 `SKILL.md` files readable through the junction. (The Windows count includes one dotfile that
> POSIX `ls` hides — not a discrepancy.)
>
> These junctions hold **absolute** targets. Moving or renaming the vault breaks all four — re-run
> the fix block above after any relocation.

## Platform-Specific Context Files

| AI Assistant | Root Context | Skills Access     |
| ------------ | ------------ | ----------------- |
| Claude Code  | `CLAUDE.md`  | `.claude/skills/` |
| Gemini       | `GEMINI.md`  | `.gemini/skills/` |
| Codex CLI    | —            | `.codex/skills/`  |

All platforms read universal context from `AGENTS.md`.

---

**Last Updated**: 2026-08-12 — added the Windows-resolvable-link requirement for Claude Cowork
after all four vault links were found to be WSL-only (reparse tag `0xA000001D`, `0` children from
Win32), which presents as a silently empty skill list in any Windows-native client.

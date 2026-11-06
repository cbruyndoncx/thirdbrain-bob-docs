# Understanding Claude Code Permission Requests

A beginner's guide to what Claude Code is asking to do when it requests permission.
> this is using css snippets to have nice cheatsheet tabular layout in PDF
## Safety Levels

| Icon | Meaning |
|------|---------|
| ✅ | **Safe** - Read-only, no changes made |
| ⚠️ | **Caution** - Makes changes, review first |
| 🛑 | **Careful** - Can delete or modify important things |

<div style="display: flex; flex-wrap: wrap; gap: 15px;">
<div style="flex: 1; min-width: 200px;">
<h2>File Operations</h2>
<h3>Reading (✅)</h3>

| Command | Does |
|---------|------|
| `cat file` | View contents |
| `head file` | First lines |
| `tail file` | Last lines |
| `less file` | Browse file |

<h3>Creating (⚠️)</h3>

| Command | Does |
|---------|------|
| `touch file` | Empty file |
| `echo > file` | Overwrite |
| `echo >> file` | Append |
| `cp a b` | Copy |
| `mkdir dir` | New folder |

<h3>Moving (⚠️)</h3>

| Command | Does |
|---------|------|
| `mv a b` | Rename/move |
| `mv f dir/` | Move to dir |

<h3>Deleting (🛑)</h3>

| Command | Does |
|---------|------|
| `rm file` | Delete |
| `rm -r dir` | Delete dir |
| `rm -rf dir` | Force delete |

<p><code>rm -rf</code> is PERMANENT!</p>
</div>
<div style="flex: 1; min-width: 200px;">
<h2>Navigation</h2>
<h3>Explore (✅)</h3>

| Command | Does |
|---------|------|
| `ls` | List files |
| `ls -la` | List all |
| `pwd` | Show path |
| `cd dir` | Change dir |
| `find` | Search |
| `tree` | Structure |

<h3>Search (✅)</h3>

| Command | Does |
|---------|------|
| `grep text` | Find text |
| `grep -r` | Find all |
| `rg pattern` | Fast find |

<h2>Run Code (⚠️)</h2>

| Command | Does |
|---------|------|
| `node x.js` | JavaScript |
| `python x.py` | Python |
| `./script.sh` | Shell |
| `chmod +x` | Executable |

<h2>Build (⚠️)</h2>

| Command | Does |
|---------|------|
| `npm build` | Build |
| `npm test` | Test |
| `pytest` | Py tests |
| `make` | Makefile |

</div>
<div style="flex: 1; min-width: 200px;">
<h2>Git</h2>
<h3>Safe (✅)</h3>

| Command | Does |
|---------|------|
| `git status` | Changes |
| `git log` | History |
| `git diff` | Diffs |
| `git branch` | Branches |

<h3>Changes (⚠️)</h3>

| Command | Does |
|---------|------|
| `git add .` | Stage all |
| `git commit` | Save |
| `git checkout` | Switch |
| `git stash` | Stash |

<h3>Network (⚠️)</h3>

| Command | Does |
|---------|------|
| `git pull` | Download |
| `git push` | Upload |
| `git fetch` | Check |
| `git clone` | Clone |

<h3>Danger (🛑)</h3>

| Command | Does |
|---------|------|
| `reset --hard` | Discard |
| `push --force` | Overwrite |
| `clean -fd` | Del untracked |

<p>You could lose work!</p>
</div>
<div style="flex: 1; min-width: 200px;">
<h2>Packages</h2>
<h3>npm (⚠️)</h3>

| Command | Does |
|---------|------|
| `npm install` | Install |
| `npm run x` | Run script |
| `npx cmd` | Run once |

<h3>pip (⚠️)</h3>

| Command | Does |
|---------|------|
| `pip install` | Install |
| `pip -r req` | All deps |
| `uv pip` | Fast |

<h3>System (🛑)</h3>

| Command | Does |
|---------|------|
| `sudo apt` | Admin! |

<h2>Network (⚠️)</h2>

| Command | Does |
|---------|------|
| `curl url` | Fetch |
| `wget url` | Download |

<h2>Process</h2>

| Command | Does |
|---------|------|
| `ps aux` | List (✅) |
| `kill PID` | Stop (⚠️) |
| `killall` | Stop all (🛑) |

</div>
</div>

---

<div style="display: flex; flex-wrap: wrap; gap: 15px;">
<div style="flex: 1; min-width: 200px;">
<h2>Environment (✅)</h2>

| Command | Does |
|---------|------|
| `echo $VAR` | Check var |
| `export V=x` | Set var |
| `env` | List all |

</div>
<div style="flex: 1; min-width: 200px;">
<h2>Compound</h2>

| Syntax | Meaning |
|--------|---------|
| `a && b` | b if a ok |
| `a \|\| b` | b if a fail |
| `a ; b` | Both run |
| `a \| b` | Pipe |

</div>
<div style="flex: 1; min-width: 200px;">
<h2>Red Flags 🚩</h2>

| Pattern | Risk |
|---------|------|
| `sudo` | Admin |
| `rm -rf /` | Delete all |
| `chmod 777` | Open |
| `curl\|bash` | Unknown |
| `--force` | Bypass |
| `eval` | Arbitrary |

</div>
<div style="flex: 1; min-width: 200px;">
<h2>You Can Always</h2>
<ol>
<li>Ask Claude to explain</li>
<li>Deny & ask alternative</li>
<li>Modify the command</li>
<li>Check paths first</li>
</ol>
</div>
</div>

---

## Quick Decision Guide

```
┌─────────────────────────────────────────────┐
│  Claude is asking to run a command...       │
├─────────────────────────────────────────────┤
│                                             │
│  READ-ONLY? (ls, cat, grep, git log)        │
│  └─► ✅ Usually safe                        │
│                                             │
│  CREATE new files?                          │
│  └─► ⚠️ Check the path                      │
│                                             │
│  MODIFY existing files?                     │
│  └─► ⚠️ Want those changes?                 │
│                                             │
│  DELETE anything?                           │
│  └─► 🛑 Double-check path!                  │
│                                             │
│  Uses SUDO?                                 │
│  └─► 🛑 Trust the command?                  │
│                                             │
│  DOWNLOAD from internet?                    │
│  └─► ⚠️ URL trustworthy?                    │
│                                             │
│  Not sure? Ask Claude to explain first!     │
│                                             │
└─────────────────────────────────────────────┘
```


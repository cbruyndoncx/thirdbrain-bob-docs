---
title: Obsidian CLI Setup
---

# Obsidian CLI Setup

Obsidian 1.12+ ships a built-in CLI that lets AI agents read, create, search, and manage vault notes. This is the preferred channel for agent ↔ vault interaction.

---

## Setup Steps

1. **Update Obsidian** to 1.12+ (Help → Check for updates)
2. **Enable CLI**: Settings → General → Advanced → **Command line interface** → ON
3. **Add to PATH**:

**Windows** (PowerShell as admin):
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\Obsidian", "Machine")
```

**macOS** (add to `~/.zshrc`):
```bash
export PATH="/Applications/Obsidian.app/Contents/MacOS:$PATH"
```

4. **Restart your terminal** for PATH changes to take effect
5. **Verify**: `obsidian help` should show available commands

---

## WSL Users — Important

!!! warning "Do NOT install Obsidian CLI on Linux from WSL"
    The CLI must run on the same OS as your Obsidian app. From WSL, call the **Windows** CLI via cmd.exe:
    ```bash
    /mnt/c/Windows/System32/cmd.exe /c "obsidian read file=Note vault=my-vault"
    ```
    Installing Obsidian on WSL will launch a separate Linux instance — it cannot control your Windows Obsidian.


---

## Related

- getting_started — Full installation guide
- [agent-client-installation](AI-Tools/agent-client-installation.md) — ACP plugin (alternative integration channel)

# Linux Bash Cheatsheet for Beginners

## Navigation

| Command | What it does | Example |
|---------|--------------|---------|
| `pwd` | Print working directory (where am I?) | `pwd` |
| `ls` | List files and folders | `ls` |
| `ls -la` | List ALL files (including hidden) with details | `ls -la` |
| `cd folder` | Change directory (go into folder) | `cd Documents` |
| `cd ..` | Go up one level (parent folder) | `cd ..` |
| `cd ~` | Go to home directory | `cd ~` |
| `cd -` | Go back to previous directory | `cd -` |

## Files & Folders

| Command | What it does | Example |
|---------|--------------|---------|
| `mkdir name` | Make a new directory | `mkdir my-project` |
| `touch file` | Create empty file | `touch notes.txt` |
| `cp source dest` | Copy file | `cp file.txt backup.txt` |
| `cp -r src dest` | Copy folder (recursive) | `cp -r folder1 folder2` |
| `mv old new` | Move or rename | `mv old.txt new.txt` |
| `rm file` | Delete file (careful!) | `rm unwanted.txt` |
| `rm -r folder` | Delete folder and contents | `rm -r old-folder` |
| `rm -rf folder` | Force delete (DANGEROUS!) | `rm -rf folder` |

## Viewing Files

| Command | What it does | Example |
|---------|--------------|---------|
| `cat file` | Print entire file | `cat notes.txt` |
| `head file` | Show first 10 lines | `head log.txt` |
| `head -n 20 file` | Show first 20 lines | `head -n 20 log.txt` |
| `tail file` | Show last 10 lines | `tail log.txt` |
| `tail -f file` | Follow file (live updates) | `tail -f server.log` |
| `less file` | Scrollable viewer (q to quit) | `less bigfile.txt` |

## Searching

| Command | What it does | Example |
|---------|--------------|---------|
| `grep "text" file` | Find text in file | `grep "error" log.txt` |
| `grep -r "text" .` | Search recursively in folder | `grep -r "TODO" .` |
| `grep -i "text" file` | Case-insensitive search | `grep -i "Error" log.txt` |
| `find . -name "*.txt"` | Find files by name | `find . -name "*.md"` |

## Permissions

| Command | What it does | Example |
|---------|--------------|---------|
| `chmod +x file` | Make file executable | `chmod +x script.sh` |
| `chmod 755 file` | rwx for owner, rx for others | `chmod 755 script.sh` |
| `chown user file` | Change file owner | `chown john file.txt` |

## Useful Shortcuts

| Shortcut | What it does |
|----------|--------------|
| `Tab` | Auto-complete file/folder names |
| `Ctrl + C` | Cancel current command |
| `Ctrl + L` | Clear screen |
| `Ctrl + R` | Search command history |
| `↑ / ↓` | Navigate command history |
| `!!` | Repeat last command |
| `sudo !!` | Repeat last command as admin |

## Pipes & Redirection

| Symbol | What it does | Example |
|--------|--------------|---------|
| `\|` | Send output to another command | `ls \| grep ".txt"` |
| `>` | Write output to file (overwrite) | `echo "hi" > file.txt` |
| `>>` | Append output to file | `echo "more" >> file.txt` |
| `<` | Read input from file | `sort < names.txt` |

## System Info

| Command | What it does |
|---------|--------------|
| `whoami` | Show current username |
| `hostname` | Show computer name |
| `df -h` | Disk space (human readable) |
| `du -sh folder` | Folder size |
| `free -h` | Memory usage |
| `top` | Running processes (q to quit) |
| `htop` | Better process viewer (if installed) |

## Package Management (Ubuntu/Debian)

| Command | What it does |
|---------|--------------|
| `sudo apt update` | Update package lists |
| `sudo apt upgrade` | Upgrade installed packages |
| `sudo apt install name` | Install a package |
| `sudo apt remove name` | Remove a package |

## Networking

| Command | What it does |
|---------|--------------|
| `ping google.com` | Test connection |
| `curl url` | Fetch URL content |
| `wget url` | Download file from URL |
| `ip addr` | Show IP addresses |

## Pro Tips

1. **Use Tab completion** - Type first few letters, press Tab
2. **Use `man command`** - Read the manual for any command
3. **Use `command --help`** - Quick help for most commands
4. **Start with `ls`** - Always know what's in your folder
5. **Be careful with `rm`** - There's no recycle bin!
6. **Use `sudo` sparingly** - Only when you need admin rights

## Common Patterns

```bash
# Find and delete all .tmp files
find . -name "*.tmp" -delete

# Count lines in a file
wc -l filename.txt

# Sort and show unique lines
sort file.txt | uniq

# Download and extract tar.gz
wget url.tar.gz && tar -xzf file.tar.gz

# Watch a command run every 2 seconds
watch -n 2 "command"
```

---

**Remember**: When in doubt, use `man command` or `command --help`!

---
layout: default
title: PowerShell
permalink: /command-line/powershell/
---

# PowerShell 🧙

The modern shell built on **.NET**. Cmdlets follow a `Verb-Noun` naming pattern, and everything is an object you can pipe around.

---

## 1. Opening It

| Way | How |
|---|---|
| Windows Terminal | Press `Win + X` → **Terminal** (profile: PowerShell) |
| Start menu | Search **"PowerShell"** or **"Terminal"** |
| From CMD | Type `powershell` (Windows PowerShell 5.1) or `pwsh` (PowerShell 7) |

> **Tip:** Most Bash/CMD habits still work because of built-in aliases: `ls`, `cd`, `cat`, `pwd`, `rm`, `cp`, `mv`, `ps`.

---

## 2. Cmdlet Basics

```powershell
Get-Command            # list available commands
Get-Command *process*  # search commands by name
Get-Help Get-Process                 # built-in help
Get-Help Get-Process -Examples       # with examples
Get-Help Get-Process -Online         # opens docs in browser
```

---

## 3. Navigation

```powershell
Get-Location      # show current path (alias: pwd)
Set-Location C:\Users\Dante\Documents   # change folder (alias: cd)
cd ..             # go up one level
cd ~              # go to your home folder (same as cd $HOME)
Set-Location D:\  # switch drives works directly
```

---

## 4. Files & Folders

```powershell
Get-ChildItem                    # list files (aliases: ls, dir)
Get-ChildItem -Force             # include hidden/os files
Get-ChildItem -Recurse           # list recursively
Get-ChildItem *.log              # filter by name pattern
Get-ChildItem | Sort-Object Length -Descending

New-Item -ItemType Directory -Path C:\new\folder   # mkdir
New-Item -ItemType File -Path notes.txt            # create empty file

Copy-Item a.txt b.txt            # copy (alias: cp, copy)
Copy-Item -Recurse src dst       # copy folder tree
Move-Item a.txt docs\            # move (alias: mv)
Rename-Item old.txt new.txt      # rename (alias: ren)
Remove-Item a.txt                # delete (alias: rm, del)
Remove-Item -Recurse -Force folder
```

---

## 5. Reading Files

```powershell
Get-Content file.txt            # print file (aliases: cat, type)
Get-Content file.txt -Tail 20   # last 20 lines, like tail -n 20
Get-Content app.log -Wait       # follow a log live, like tail -f
Get-Content file.txt -Head 10   # first 10 lines
```

---

## 6. The Pipeline (the superpower)

Everything PowerShell returns is an **object**, and `|` passes it along:

```powershell
# Top 5 processes by CPU
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5

# Files bigger than 1 MB
Get-ChildItem | Where-Object Length -gt 1MB

# Running services
Get-Service | Where-Object Status -eq Running

# Nicely formatted tables and full detail
Get-Process | Format-Table Name, CPU, WorkingSet
Get-Process | Format-List *
```

Common pipeline cmdlets: `Where-Object` (filter), `Select-Object` (pick columns / -First N), `Sort-Object`, `ForEach-Object`, `Format-Table` / `Format-List`.

---

## 7. Aliases

```powershell
Get-Alias                      # list every alias
Get-Alias ls                   # show what 'ls' really does
New-Alias ll Get-ChildItem     # create your own
```

Common built-ins: `ls`/`dir` = `Get-ChildItem`, `cd` = `Set-Location`, `cat`/`type` = `Get-Content`, `pwd` = `Get-Location`, `ps` = `Get-Process`, `cp` = `Copy-Item`, `mv` = `Move-Item`, `rm`/`del` = `Remove-Item`, `cls`/`clear` = `Clear-Host`, `ping` = `Test-Connection`.

---

## 8. Variables & Environment

```powershell
$name = "Dante"              # create a variable
Write-Host "Hello $name"     # print it
echo $name                   # Write-Output shortcut

$env:Path                    # show PATH environment variable
$env:Path += ";C:\myapp\bin" # append to PATH (session only)
Get-ChildItem Env:           # list all environment variables
$HOME                        # your user folder
$PSVersionTable              # PowerShell version info
```

---

## 9. Networking

```powershell
Test-Connection google.com          # ping (alias: ping)
Test-Connection -Count 4 8.8.8.8
Resolve-DnsName google.com          # DNS lookup (like nslookup)
Get-NetIPAddress                    # your IP configuration
Get-NetAdapter                      # network adapters
ipconfig                            # native commands still work too
```

---

## 10. Processes & Services

```powershell
Get-Process                    # all processes
Get-Process notepad            # find by name
Get-Process -Id 1234           # find by PID
Stop-Process -Name notepad -Force   # kill by name
Stop-Process -Id 1234 -Force        # kill by PID
Restart-Service sshd                # services work the same way
```

---

## 11. History & Profile

```powershell
Get-History             # session command history
h                      # shortcut for Get-History
Invoke-History 5        # re-run entry #5
$PROFILE                # path to your PowerShell profile
notepad $PROFILE        # edit it (create it first if missing)
```

For safety, run without a step first:

```powershell
Remove-Item -Recurse -Force .\old -WhatIf   # preview, not delete
```

---

## 12. Handy Keys

| Keys | Action |
|---|---|
| `↑` / `↓` | Previous / next command |
| `Ctrl + R` | Reverse search through history |
| `Tab` | Autocomplete (menu with repeated presses) |
| `Ctrl + C` | Interrupt current command |
| `F8` | Cycle through matching history |
| `Ctrl + L` | Clear screen |

---

> See also: [Command Prompt](../cmd/), [Bash (Linux & macOS)](../bash/), [Cross-Shell Cheat Sheet](../cheat-sheet/)

<!-- 愛をこめて ダンテが作りました -->
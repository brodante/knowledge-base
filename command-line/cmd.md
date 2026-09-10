---
layout: default
title: Command Prompt & Windows Terminal
permalink: /command-line/cmd/
---

# Command Prompt & Windows Terminal 🪟

Everything you need for the classic Windows **Command Prompt** (`cmd.exe`), best used inside the modern **Windows Terminal** app.

---

## 1. Opening It

| Way | How |
|---|---|
| Run dialog | Press `Win + R`, type `cmd`, press Enter |
| Start menu | Search **"Command Prompt"** or **"Terminal"** |
| From Explorer | In a folder, click the address bar, type `cmd`, Enter |

> **Tip:** Windows Terminal can host CMD, PowerShell, and even WSL/Bash side by side in tabs. Run `wt` from a Run dialog or terminal to start it.

---

## 2. Navigation

```bat
cd            REM show current directory
cd ..         REM go up one folder
cd /d D:\proj REM change drive AND folder
pushd D:\x    REM save current dir, jump to D:\x
popd          REM return to saved dir
```

## 3. Files & Folders

```bat
dir                     REM list files
dir /a                  REM include hidden/system files
dir /s                  REM list recursively
tree /f                 REM visual folder tree
mkdir new\folder\name   REM create folders (creates all levels)
copy a.txt b.txt        REM copy file
robocopy src dst /E     REM robust copy of whole folders
move a.txt docs\        REM move file
ren old.txt new.txt     REM rename
del a.txt               REM delete file
rmdir docs              REM remove empty folder
rmdir /s /q docs        REM remove folder + contents (no prompt)
```

## 4. Viewing Files

```bat
type file.txt    REM print file to screen
more file.txt    REM page through a big file (Space, Q to quit)
```

## 5. Networking

```bat
ipconfig           REM your IP configuration
ipconfig /all      REM full detail (MAC, DNS, gateway)
ipconfig /flushdns REM clear DNS cache
ping google.com    REM test connectivity
ping -t 8.8.8.8    REM ping forever, Ctrl+C to stop
tracert google.com REM show route hops
nslookup google.com
netstat -ano       REM connections + owning PID
netstat -ano | findstr LISTENING
```

## 6. Processes & System

```bat
tasklist                  REM list running processes
tasklist | findstr notepad
taskkill /IM notepad.exe /F   REM kill by name, force
taskkill /PID 1234 /F         REM kill by PID
systeminfo                REM hardware + OS info
whoami                    REM current user
ver                       REM Windows version
cls                       REM clear screen
```

## 7. Clipboard

```bat
dir | clip          REM copy command output to clipboard
clip < file.txt     REM copy file content to clipboard
echo hi | clip
```

## 8. Redirects & Pipes

```bat
dir > listing.txt   REM save output to file (overwrite)
dir >> listing.txt  REM append to file
command 2> err.txt  REM capture errors
command >nul        REM throw output away
dir | more          REM pipe output through pager
dir | findstr txt   REM pipe into search
```

**Searching text:** `findstr` is the CMD cousin of grep:

```bat
findstr /i "error" log.txt
findstr /s /i "TODO" *.java
```

## 9. Environment Variables

```bat
echo %PATH%                    REM show PATH
set                            REM list all variables
set MYVAR=hello                REM set (session only)
echo %MYVAR%
set PATH=%PATH%;C:\myapp\bin   REM append to PATH
```

## 10. Batch Files (`.bat`)

```bat
@echo off
echo Hello %USERNAME%!
echo Your folder: %CD%
pause
```

A quick loop:

```bat
@echo off
for /L %%i in (1,1,5) do echo Count: %%i
pause
```

- `%1`, `%2` — first/second argument passed to the script
- `if exist file.txt echo Found` — conditional
- Save as `myscript.bat` and run with `myscript` or `myscript.bat`

## 11. Handy Keys

| Keys | Action |
|---|---|
| `Tab` | Autocomplete file/folder names (press repeatedly to cycle) |
| `F7` | See command history as a list |
| `↑` / `↓` | Previous / next command |
| `Ctrl + C` | Interrupt a running command |
| `Ctrl + V` / right-click | Paste (in Windows Terminal) |
| `Ctrl + L` | Clear screen (Windows Terminal) |

---

> See also: [PowerShell](../powershell/), [Bash (Linux & macOS)](../bash/), [Cross-Shell Cheat Sheet](../cheat-sheet/)

<!-- 愛をこめて ダンテが作りました -->
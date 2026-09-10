---
layout: default
title: Cross-Shell Cheat Sheet
permalink: /command-line/cheat-sheet/
---

# Cross-Shell Cheat Sheet 🔁

The same everyday task, in **Command Prompt**, **PowerShell**, and **Bash**. Aliases shown in parentheses work too.

---

## Navigation & Files

| Task | Windows CMD | PowerShell | Bash |
|---|---|---|---|
| Show current folder | `` cd `` | `` Get-Location `` (`` pwd ``) | `` pwd `` |
| List files | `` dir `` | `` Get-ChildItem `` (`` ls ``) | `` ls `` |
| List hidden files | `` dir /a `` | `` Get-ChildItem -Force `` | `` ls -la `` |
| Change folder | `` cd path `` | `` Set-Location path `` (`` cd ``) | `` cd path `` |
| Go up one folder | `` cd .. `` | `` cd .. `` | `` cd .. `` |
| Go home | `` cd %USERPROFILE% `` | `` cd ~ `` | `` cd ~ `` |
| Clear screen | `` cls `` | `` Clear-Host `` (`` cls ``) | `` clear `` |
| Copy a file | `` copy a b `` | `` Copy-Item a b `` (`` cp ``) | `` cp a b `` |
| Copy a folder | `` robocopy src dst /E `` | `` Copy-Item -Recurse src dst `` | `` cp -r src dst `` |
| Move a file | `` move a b `` | `` Move-Item a b `` (`` mv ``) | `` mv a b `` |
| Delete a file | `` del a `` | `` Remove-Item a `` (`` rm ``) | `` rm a `` |
| Delete a folder | `` rmdir /s /q d `` | `` Remove-Item -Recurse -Force d `` | `` rm -rf d `` |
| Make a folder | `` mkdir d `` | `` New-Item -ItemType Directory d `` | `` mkdir -p d `` |
| Rename | `` ren old new `` | `` Rename-Item old new `` | `` mv old new `` |
| Create empty file | `` type nul > f.txt `` | `` New-Item f.txt `` | `` touch f.txt `` |

---

## Viewing & Searching

| Task | Windows CMD | PowerShell | Bash |
|---|---|---|---|
| Print a file | `` type f `` | `` Get-Content f `` (`` cat ``) | `` cat f `` |
| Page through a file | `` more f `` | `` Get-Content f `` | `` less f `` |
| First N lines | — | `` Get-Content f -Head N `` | `` head -n N f `` |
| Last N lines | — | `` Get-Content f -Tail N `` | `` tail -n N f `` |
| Follow a live log | — | `` Get-Content f -Wait `` | `` tail -f f `` |
| Search text | `` findstr /i "p" f `` | `` Select-String -Pattern p f `` | `` grep -i p f `` |
| Search recursively | `` findstr /s /i "p" *.* `` | `` Get-ChildItem -Recurse \| Select-String p `` | `` grep -ri p . `` |
| Count lines | `` find /c "" f `` | `` (Get-Content f).Count `` | `` wc -l f `` |

---

## Environment & Output

| Task | Windows CMD | PowerShell | Bash |
|---|---|---|---|
| Show PATH | `` echo %PATH% `` | `` $env:Path `` | `` echo $PATH `` |
| List all env vars | `` set `` | `` Get-ChildItem Env: `` | `` env `` |
| Set a variable | `` set X=y `` | `` $env:X = "y" `` | `` export X=y `` |
| Run history | `` doskey /history `` | `` Get-History `` | `` history `` |
| Reverse history search | `` F7 `` | `` Ctrl + R `` | `` Ctrl + R `` |
| Save output to file | `` c > out.txt `` | `` c > out.txt `` | `` c > out.txt `` |
| Append output to file | `` c >> out.txt `` | `` c >> out.txt `` | `` c >> out.txt `` |

---

## Processes & System

| Task | Windows CMD | PowerShell | Bash |
|---|---|---|---|
| List processes | `` tasklist `` | `` Get-Process `` (`` ps ``) | `` ps aux `` |
| Find a process | `` tasklist \| findstr n `` | `` Get-Process n `` | `` ps aux \| grep n `` |
| Kill a process | `` taskkill /IM n.exe /F `` | `` Stop-Process -Name n -Force `` | `` pkill n `` |
| Kill by PID | `` taskkill /PID 1234 /F `` | `` Stop-Process -Id 1234 -Force `` | `` kill 1234 `` |
| Current user | `` whoami `` | `` whoami `` | `` whoami `` |
| System info | `` systeminfo `` | `` Get-ComputerInfo `` | `` uname -a `` |
| Disk usage | `` wmic logicaldisk `` | `` Get-PSDrive C `` | `` df -h `` |

---

## Networking

| Task | Windows CMD | PowerShell | Bash |
|---|---|---|---|
| Ping a host | `` ping host `` | `` Test-Connection host `` | `` ping -c 4 host `` |
| Your IP config | `` ipconfig `` | `` Get-NetIPAddress `` | `` ip a `` |
| DNS lookup | `` nslookup host `` | `` Resolve-DnsName host `` | `` dig host `` |
| Listening ports | `` netstat -ano `` | `` Get-NetTCPConnection `` | `` ss -tulpn `` |
| Download a URL | — | `` Invoke-WebRequest URL `` | `` curl URL `` |

---

## Choose Your Shell

| You want... | Use |
|---|---|
| Windows only, simple scripts | [Command Prompt](../cmd/) |
| Automation, objects, .NET power | [PowerShell](../powershell/) |
| Linux servers, macOS, WSL | [Bash](../bash/) |

---

<!-- 愛をこめて ダンテが作りました -->
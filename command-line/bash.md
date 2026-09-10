---
layout: default
title: Bash
permalink: /command-line/bash/
---

# Bash (Linux, Git Bash, macOS) 🐚

The standard shell on Linux (Bash), available on Windows through **WSL** or **Git Bash**, and nearly identical in **macOS**'s Terminal (zsh). If you learn Bash, you can use almost any Unix system.

---

## 1. Opening It

| System | How |
|---|---|
| Linux (Ubuntu etc.) | Press `Ctrl + Alt + T` |
| Windows | Install **WSL** → run `wsl`; or install **Git Bash** and launch it |
| macOS | Applications → Utilities → **Terminal** |

---

## 2. Navigation

```bash
pwd          # print working directory (where am I?)
ls           # list files
ls -la       # long format, all files (including hidden .files)
ls -lh       # human-readable sizes
cd documents # change into folder
cd ..        # go up one level
cd ~         # go home
cd -         # back to the previous folder
```

---

## 3. Files & Folders

```bash
cp file.txt copy.txt      # copy file
cp -r src dst             # copy a whole folder
mv file.txt notes/        # move
mv old.txt new.txt        # rename
rm file.txt               # delete file
rm -rf folder             # delete folder + everything inside (be careful!)
mkdir projects            # make folder
mkdir -p a/b/c            # make nested folders at once
touch notes.txt           # create empty file / update timestamp
file notes.txt            # show what kind of file it is
ln -s /real/path link     # create a symlink
```

---

## 4. View & Search Text

```bash
cat notes.txt             # print whole file
less notes.txt            # page through (q to quit, / to search)
head -n 20 notes.txt      # first 20 lines
tail -f app.log           # follow log file live
wc -l notes.txt           # count lines

grep error log.txt                     # find lines matching "error"
grep -ri "password" ~/projects         # recursive, case-insensitive
grep -E "err|warn" log.txt             # extended regex
```

---

## 5. Permissions

```bash
ls -l script.sh          # show permissions: -rwxr-xr-x
chmod +x script.sh       # make executable
chmod 755 script.sh      # rwx for owner, rx for others
chmod -R 755 folder      # apply recursively
./script.sh              # run a script in the current folder
```

---

## 6. Pipes & Redirects

```bash
ls | grep txt                    # feed output into another command
ps aux | grep ssh                # find a process
cat log.txt | head -n 5

ls > files.txt                   # save output to file (overwrite)
ls >> files.txt                  # append to file
command 2> errors.txt            # capture errors only
command &> all.txt               # capture both output and errors
command > /dev/null              # discard output
```

---

## 7. Processes & Jobs

```bash
ps aux                    # all processes
ps aux | grep mysql       # find one
top                       # live view (q to quit)
htop                      # nicer live view, if installed

kill 1234                 # ask process 1234 to stop
kill -9 1234              # force kill (last resort)
pkill firefox             # kill by name

sleep 30 &                # run in the background
jobs                      # list background jobs
fg                        # bring a job to the foreground
```

---

## 8. Networking

```bash
ping -c 4 google.com       # 4 pings (Linux); macOS: ping google.com
curl https://example.com   # download/fetch a URL to stdout
wget https://example.com   # download a file
ip a                       # show IP addresses (modern)
ifconfig                   # older tool, still on macOS
ss -tulpn                  # listening ports and programs
ssh user@server            # log into a remote machine
```

---

## 9. System Info & Disk

```bash
whoami        # current user
uname -a      # kernel info
df -h         # disk usage by filesystem
du -sh *      # folder sizes in the current directory
free -h       # memory usage
uptime        # how long the machine has been up
sudo ls /root # run a command as administrator
```

---

## 10. Package Managers

| System | Command |
|---|---|
| Debian/Ubuntu | `sudo apt update && sudo apt install htop` |
| Fedora/RHEL | `sudo dnf install htop` |
| Arch | `sudo pacman -S htop` |
| macOS (Homebrew) | `brew install htop` |

---

## 11. Environment & Shell Config

```bash
echo $SHELL       # which shell is running
echo $PATH        # where executables live
export MYVAR=hello        # set a variable (session only)
echo $MYVAR

export PATH="$HOME/bin:$PATH"   # add a folder to PATH
```

Persist settings in `~/.bashrc` (Linux/Git Bash) or `~/.zshrc` (macOS):

```bash
nano ~/.bashrc        # edit
source ~/.bashrc      # reload without restarting
```

---

## 12. History & Shortcuts

```bash
history          # show history
!123             # re-run history entry 123
!!               # re-run the last command
sudo !!          # re-run last command as root
```

| Keys | Action |
|---|---|
| `Ctrl + R` | Reverse search through history |
| `Tab` | Autocomplete (files, commands, flags) |
| `Ctrl + A` / `Ctrl + E` | Jump to start / end of line |
| `Ctrl + U` / `Ctrl + K` | Delete to start / end of line |
| `Ctrl + W` | Delete previous word |
| `Ctrl + L` | Clear screen |
| `Ctrl + C` | Cancel current command |
| `Ctrl + D` | Exit shell |

---

## 13. Wildcards & Expansion

```bash
ls *.txt                  # every .txt file
rm photo?.jpg             # photo1.jpg, photoA.jpg, ...
cp *.png backups/         # copy all PNGs
echo {1,2,3}              # prints: 1 2 3
echo {1..5}               # prints: 1 2 3 4 5
```

---

> See also: [Command Prompt](../cmd/), [PowerShell](../powershell/), [Cross-Shell Cheat Sheet](../cheat-sheet/)

<!-- 愛をこめて ダンテが作りました -->
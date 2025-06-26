# sink-switch
---

A lightweight, dependency-free Bash script to switch between connected audio output sinks on systems using PulseAudio or PipeWire. It dynamically detects all available sinks and allows switching via cycling, direct set, or querying the current sink — with optional desktop notifications.

---

## Dependencies
---

- `bash`
- `pactl` (from `pulseaudio-utils` or `pipewire-pulseaudio`)
- `libnotify` (for `notify-send`, optional)

All dependencies are likely preinstalled on most Fedora systems using PipeWire.

---

## Installation
---

### 🔧 Fedora (via COPR):

```bash
sudo dnf copr enable yourusername/sink-switch
sudo dnf install sink-switch
```

## Usage
--- 

```bash
sink-switch                  # Switch to the next sink
sink-switch --previous      # Switch to the previous sink
sink-switch --set <name>    # Switch to sink by exact name
sink-switch --current       # Print current default sink
sink-switch --list          # List all currently available sinks
sink-switch --no-notify     # Disable desktop notification
```

### 💡Tip: Set Keyboard Shortcut
For quick switching, bind this script to a keyboard shortcut in your desktop environment:

KDE: System Settings → Shortcuts → Custom Shortcuts
GNOME: Settings → Keyboard → Custom Shortcuts

You can bind these commands to some keys like `Super + Shift + F11` or `Super + Shift + F10`

```
sink-switch --next
sink-switch --previous
```

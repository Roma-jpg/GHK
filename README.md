# Global Hotkey Kernel (GHK)

**GHK** is a lightweight Python-based tool that lets you map global keyboard shortcuts to your custom Python functions or external programs. It runs silently in the background and reacts instantly to your key combinations.

GHK was made for personal productivity and automation.

## 💻 Features

* Global keyboard shortcut listener
* Easy configuration via `shortcuts.json`
* Custom function execution
* Toast notification on startup
* Cooldown system to prevent accidental multiple activations
* Portable and super lightweight

## 🚀 Requirements

* Python 3.9+
* Libraries:

  * `keyboard`
  * `win10toast`

Install them via:

```
pip install keyboard win10toast
```

## ⚙️ Usage

1. Clone or download the repository.
2. Place your `shortcuts.json` file in the same folder as `main.py`.
3. Run `main.py`.

You will get a Windows notification when the tool is ready.

## 🎛️ shortcuts.json structure

Example `shortcuts.json`:

```json
{
    "win+alt+shift+t": "test_notification",
    "ctrl+alt+shift+w": "open_work_apps"
}
```

Each key combination triggers the corresponding function name.

## 📥 Built-in Functions

* `test_notification()`: Shows a test Windows toast notification.
* `open_work_apps()`: Launches your most used programs. (Hardcoded paths, modify in code)

## 💡 Pro Tips

* To avoid Windows conflicts, prefer combos like `ctrl+alt+shift+X` or `win+alt+shift+X`.
* You can run GHK on startup by creating a `.bat` file in the Windows startup folder. You can access it using Win+R and typing "shell:startup".

Example batch:

```bat
@echo off
chcp 1251 >nul
start "" pythonw "C:\Path\To\GHK.py"
exit
```

## ❗ Notes

* Do not forget to replace hardcoded paths (`open_work_apps()`) with your actual program locations.

## 🛠️ Disclaimer

This project was made for fun and personal use. Use at your own risk.
The author is not responsible for any possible damage caused by this program

# 🧠 NoxBoot

**Smart Startup Manager for Linux — because your boot deserves better.**  
NoxBoot lets you easily list, enable, or disable startup apps right from the terminal.  
Lightweight, fast, and perfect for people who love a clean boot.

---

## ⚡ Features

- 🔍 List all startup applications  
- 🚫 Disable or re-enable apps instantly  
- 🧠 Status overview (enabled/disabled)  
- 🧩 Simple YAML-based config system  
- 🌈 Customizable colors and themes  

---

## 🧩 Installation

### **AUR (Arch / Manjaro)**
```bash
yay -S noxboot
````

### **From source**

```bash
git clone https://github.com/pvk-96/noxboot.git
cd noxboot
python -m noxboot.cli
```

---

## 🚀 Usage

```bash
noxboot list         # List startup apps
noxboot status       # Show enabled/disabled status
noxboot disable app  # Disable an app
noxboot enable app   # Re-enable an app
```

Example:

```bash
noxboot disable discord
noxboot enable discord
```

---

## 🧱 Config File

Located at:
`~/.config/noxboot/config.yaml`

You can customize:

* `theme`
* `colors.banner`, `colors.accent`, `colors.text`
* `log_actions`

Example:

```yaml
theme: dark
colors:
  banner: magenta
  accent: cyan
  text: white
log_actions: true
```

---

## 🛠️ Requirements

* Python ≥ 3.10
* Typer ≥ 0.9
* Rich ≥ 13.0
* Psutil ≥ 5.9
* PyYAML ≥ 6.0

---

## 💡 Example Output

```
$ noxboot status
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Status   ┃ App Name         ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Enabled  │ Discord          │
│ Disabled │ Steam            │
└──────────┴──────────────────┘
```

---

## 🧠 Feedback

Found a bug or have a feature idea?
👉 Contact here: praneethvarmakopperla@gmail.com
---

## 🧾 License

Licensed under the **MIT License** — do whatever you want, just don’t make it worse. 😎

---

### ⭐ If you like NoxBoot

Give it a star on GitHub and vote for it on the AUR!

[![AUR version](https://img.shields.io/aur/version/noxboot)](https://aur.archlinux.org/packages/noxboot)
[![AUR votes](https://img.shields.io/aur/votes/noxboot)](https://aur.archlinux.org/packages/noxboot)

```

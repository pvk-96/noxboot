"""
core.py — NoxBoot Core Logic
Handles startup app listing, enabling, disabling, and status checks.
"""

from pathlib import Path
from rich import print

AUTOSTART_DIR = Path.home() / ".config/autostart"
LOG_PATH = Path.home() / ".config/noxboot/logs.txt"


def _log_action(action: str, app_name: str):
    """Log enable/disable actions."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"{action.upper()}: {app_name}\n")


def list_startup_apps():
    """Return a list of startup app names."""
    apps = []
    if not AUTOSTART_DIR.exists():
        print("[yellow]⚠ No autostart directory found.[/yellow]")
        return []
    for file in AUTOSTART_DIR.glob("*.desktop"):
        apps.append(file.stem)
    return sorted(apps)


def disable_app(app_name: str):
    """Disable a startup app by renaming its .desktop file."""
    app_path = AUTOSTART_DIR / f"{app_name}.desktop"
    if app_path.exists():
        new_path = app_path.with_suffix(".desktop.disabled")
        app_path.rename(new_path)
        _log_action("DISABLED", app_name)
        print(f"[red]❌ Disabled:[/red] {app_name}")
    else:
        print(f"[yellow]App not found:[/yellow] {app_name}")


def enable_app(app_name: str):
    """Re-enable a disabled startup app."""
    disabled_path = AUTOSTART_DIR / f"{app_name}.desktop.disabled"
    if disabled_path.exists():
        new_path = disabled_path.with_suffix(".desktop")
        disabled_path.rename(new_path)
        _log_action("ENABLED", app_name)
        print(f"[green]✅ Enabled:[/green] {app_name}")
    else:
        print(f"[yellow]No disabled entry found for:[/yellow] {app_name}")


def app_status():
    """Return a list of tuples: (app_name, enabled: bool)."""
    apps = []
    if not AUTOSTART_DIR.exists():
        print("[yellow]⚠ No autostart directory found.[/yellow]")
        return []
    for file in AUTOSTART_DIR.glob("*.desktop*"):
        name = file.stem.replace(".desktop", "")
        enabled = not file.name.endswith(".disabled")
        apps.append((name, enabled))
    return sorted(apps)


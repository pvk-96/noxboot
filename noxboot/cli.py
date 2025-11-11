"""
cli.py — NoxBoot Command-Line Interface
Provides commands to list, enable, disable, and check status of startup apps.
"""

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import importlib.metadata
import yaml
import os
import sys
from noxboot import core
from noxboot.config import load_config, save_config, DEFAULT_CONFIG

# Load user configuration
cfg = load_config()

console = Console()
app = typer.Typer(help="NoxBoot — Smart Startup Manager CLI")

# =====================================================================
#                          ASCII BANNER
# =====================================================================

def print_banner():
    banner_color = cfg["colors"]["banner"]
    accent_color = cfg["colors"]["accent"]
    banner = r"""

 ██████   █████                      ███████████                     █████   
░░██████ ░░███                      ░░███░░░░░███                   ░░███    
 ░███░███ ░███   ██████  █████ █████ ░███    ░███  ██████   ██████  ███████  
 ░███░░███░███  ███░░███░░███ ░░███  ░██████████  ███░░███ ███░░███░░░███░   
 ░███ ░░██████ ░███ ░███ ░░░█████░   ░███░░░░░███░███ ░███░███ ░███  ░███    
 ░███  ░░█████ ░███ ░███  ███░░░███  ░███    ░███░███ ░███░███ ░███  ░███ ███
 █████  ░░█████░░██████  █████ █████ ███████████ ░░██████ ░░██████   ░░█████ 
░░░░░    ░░░░░  ░░░░░░  ░░░░░ ░░░░░ ░░░░░░░░░░░   ░░░░░░   ░░░░░░     ░░░░░  
                                                                             
                                                                             
"""
    console.print(banner, style=f"bold {banner_color}")
    console.rule(f"[bold {accent_color}]NoxBoot — Start Smart. Boot Cleaner.[/bold {accent_color}]")

print_banner()

# =====================================================================
#                         CORE COMMANDS
# =====================================================================

@app.command()
def list():
    """List enabled startup applications."""
    apps = core.list_startup_apps()
    if not apps:
        console.print("[yellow]No startup apps found.[/yellow]")
        return

    table = Table(title="[bold cyan]Enabled Startup Applications[/bold cyan]", show_lines=True)
    table.add_column("App Name", justify="left", style="bold cyan")

    for app_name in apps:
        table.add_row(app_name)
    console.print(table)


@app.command()
def disable(name: str):
    """Disable a startup app."""
    core.disable_app(name)


@app.command()
def enable(name: str):
    """Enable a previously disabled startup app."""
    core.enable_app(name)


@app.command()
def status():
    """Show enabled/disabled startup apps."""
    apps = core.app_status()
    if not apps:
        console.print("[yellow]No startup apps found.[/yellow]")
        return

    table = Table(title="[bold cyan]Startup App Status[/bold cyan]", show_lines=True)
    table.add_column("Status", justify="center", style="bold")
    table.add_column("App Name", justify="left", style="cyan")

    for name, enabled in apps:
        status_text = "[green]Enabled[/green]" if enabled else "[red]Disabled[/red]"
        table.add_row(status_text, name)
    console.print(table)


@app.command()
def version():
    """Show NoxBoot version."""
    try:
        v = importlib.metadata.version("noxboot")
        console.print(f"[bold cyan]NoxBoot v{v}[/bold cyan]")
    except importlib.metadata.PackageNotFoundError:
        console.print("[yellow]Version info not found (editable mode).[/yellow]")


# =====================================================================
#                         CONFIG COMMANDS
# =====================================================================

config_app = typer.Typer(help="View and modify NoxBoot configuration.")
app.add_typer(config_app, name="config")


@config_app.command("show")
def show_config():
    """Display current configuration."""
    console.print(
        Panel.fit(
            yaml.dump(cfg, sort_keys=False),
            title="[bold cyan]Current Configuration[/bold cyan]",
            border_style="cyan",
        )
    )


@config_app.command("set")
def set_config(key: str, value: str):
    """Update a specific configuration key (dot notation supported)."""
    parts = key.split(".")
    temp = cfg
    try:
        for part in parts[:-1]:
            temp = temp[part]
        temp[parts[-1]] = value
        save_config(cfg)
        console.print(f"[green]✔ Updated {key} = {value}[/green]")
        console.print("[dim]Restart NoxBoot manually to apply changes.[/dim]")
    except Exception as e:
        console.print(f"[red]✖ Failed to update config:[/red] {e}")


@config_app.command("reset")
def reset_config():
    """Reset configuration to default values."""
    save_config(DEFAULT_CONFIG)
    console.print("[yellow]⚠ Configuration reset to defaults.[/yellow]")
    console.print("[dim]Restart NoxBoot manually to apply changes.[/dim]")


# =====================================================================
#                           ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    app()


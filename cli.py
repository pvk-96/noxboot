print(">>> Loaded CLI from:", __file__)
"""
cli.py — NoxBoot Command-Line Interface
Provides commands to list, enable, disable, and check status of startup apps.
"""

import typer
from rich.console import Console
from rich.table import Table
import importlib.metadata
from noxboot import core

app = typer.Typer(help="NoxBoot — Start Smart. Boot Cleaner.")
console = Console()


@app.command()
def list():
    """List enabled startup applications."""
    apps = core.list_startup_apps()
    if not apps:
        console.print("[yellow]No startup apps found.[/yellow]")
        return

    table = Table(title="Enabled Startup Applications")
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

    table = Table(title="Startup App Status")
    table.add_column("Status", justify="center", style="bold")
    table.add_column("App Name", justify="left")

    for name, enabled in apps:
        status = "[green]Enabled[/green]" if enabled else "[red]Disabled[/red]"
        table.add_row(status, name)
    console.print(table)


@app.command()
def version():
    """Show NoxBoot version."""
    try:
        v = importlib.metadata.version("noxboot")
        console.print(f"[bold cyan]NoxBoot v{v}[/bold cyan]")
    except importlib.metadata.PackageNotFoundError:
        console.print("[yellow]Version info not found (run via editable install).[/yellow]")


if __name__ == "__main__":
    app()


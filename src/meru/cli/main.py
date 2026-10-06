import typer
from rich.console import Console

app = typer.Typer(help="Meru AI-native Linux runtime")
console = Console()


@app.command()
def status() -> None:
    """Show the current V0 bootstrap status."""
    console.print("[bold]Meru V0[/bold]: bootstrap ready")


if __name__ == "__main__":
    app()

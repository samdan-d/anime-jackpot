from typing import Optional

import typer

from anime_jackpot import __version__, __app_name__

app = typer.Typer()


@app.command()
def hello(name: str = "orgil"):
    print(f"Hello {name}")


def options(
  version: bool = typer.Option(False, help="Say hi formally."),
):
    if version:
        typer.echo(f"{__app_name__} v{__version__}")

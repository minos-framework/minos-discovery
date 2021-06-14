"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from pathlib import (
    Path,
)
from typing import (
    Optional,
)

import typer

from minos.api_gateway.common import (
    MinosConfig,
)

from .launchers import (
    EntrypointLauncher,
)
from .periodic import (
    DiscoveryPeriodicHealthChecker,
)
from .service import (
    DiscoveryService,
)

app = typer.Typer()


@app.command("start")
def start(
    file_path: Optional[Path] = typer.Argument(
        "config.yml", help="Discovery Service configuration file.", envvar="MINOS_API_GATEWAY_CONFIG_FILE_PATH"
    )
):  # pragma: no cover
    """Start Discovery services."""

    try:
        config = MinosConfig(file_path)
    except Exception as exc:
        typer.echo(f"Error loading config: {exc!r}")
        raise typer.Exit(code=1)

    services = (
        DiscoveryPeriodicHealthChecker(interval=120, delay=0, config=config),
        DiscoveryService(config=config),
    )
    try:
        EntrypointLauncher(config=config, services=services).launch()
    except Exception as exc:
        typer.echo(f"Error launching Discovery Service: {exc!r}")
        raise typer.Exit(code=1)

    typer.echo("Discovery Service is up and running!\n")


@app.command("status")
def status():
    """Get the Discovery Service status."""
    raise NotImplementedError


@app.command("stop")
def stop():
    """Stop the Discovery Service."""
    raise NotImplementedError


def main():  # pragma: no cover
    """CLI's main function."""
    app()

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

from .health_status import (
    HealthStatusCheckerService,
)
from .launchers import (
    EntrypointLauncher,
)
from .service import (
    DiscoveryService,
)

app = typer.Typer()

CONFIG_FILE_PATH = Path(__file__).parent / "config.yml"


@app.command("start")
def start():
    """Start Discovery services."""

    config = MinosConfig(CONFIG_FILE_PATH)

    services = (
        HealthStatusCheckerService(interval=120, delay=0, config=config),
        DiscoveryService(),
    )
    launcher = EntrypointLauncher(services=services)
    launcher.launch()


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

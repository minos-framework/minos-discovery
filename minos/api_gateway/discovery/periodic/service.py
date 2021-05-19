"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from __future__ import (
    annotations,
)

from aiomisc.service.periodic import (
    PeriodicService,
)

from minos.api_gateway.common import (
    MinosConfig,
)

from .abc import (
    HealthStatusCheck,
)


class DiscoveryPeriodicHealthChecker(PeriodicService):
    """Minos DiscoveryPeriodicHealthChecker class."""

    def __init__(self, config: MinosConfig = None, **kwargs):
        super().__init__(**kwargs)
        self.status_checker = HealthStatusCheck(config=config)

    async def start(self) -> None:
        """Method to be called at the startup by the internal ``aiomisc`` loigc.

        :return: This method does not return anything.
        """
        await super().start()  # pragma: no cover

    async def callback(self) -> None:
        """Method to be called periodically by the internal ``aiomisc`` logic.

        :return:This method does not return anything.
        """
        await self.status_checker.perform_health_check()  # pragma: no cover

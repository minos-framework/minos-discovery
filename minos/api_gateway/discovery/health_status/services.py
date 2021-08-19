from __future__ import (
    annotations,
)

from aiomisc.service.periodic import (
    PeriodicService,
)

from minos.api_gateway.common import (
    MinosConfig,
)

from .checkers import (
    HealthStatusChecker,
)


class HealthStatusCheckerService(PeriodicService):
    """Minos DiscoveryPeriodicHealthChecker class."""

    def __init__(self, config: MinosConfig = None, **kwargs):
        super().__init__(**kwargs)
        self.status_checker = HealthStatusChecker(config=config)

    async def callback(self) -> None:
        """Method to be called periodically by the internal ``aiomisc`` logic.

        :return:This method does not return anything.
        """
        await self.status_checker.check()  # pragma: no cover

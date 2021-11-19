import asyncio
import logging

from aiohttp import (
    web,
)
from aiomisc.service.aiohttp import (
    AIOHTTPService,
)

from minos.api_gateway.common import (
    MinosConfig,
)

from .database import (
    MinosRedisClient,
)
from .views import (
    routes,
)

logger = logging.getLogger(__name__)


class DiscoveryService(AIOHTTPService):
    """Discovery Service class."""

    def __init__(self, address: str, port: int, config: MinosConfig, graceful_stop_timeout: int = 5):
        self.config = config
        self.graceful_stop_timeout = graceful_stop_timeout
        logger.info(
            f"Address {address}"
            f"Port {port}"
        )
        super().__init__(address, port)

    async def create_application(self) -> web.Application:
        app = web.Application()
        app.router.add_routes(routes)

        app["db_client"] = MinosRedisClient(self.config)

        return app

    async def stop(self, exception: Exception = None) -> None:
        """

        :param exception:
        :return:
        """

        logger.info(
            f"Stopping Discovery Service gracefully "
            f"(waiting {self.graceful_stop_timeout} seconds for microservices unsubscription)..."
        )
        await asyncio.sleep(self.graceful_stop_timeout)
        await super().stop(exception)

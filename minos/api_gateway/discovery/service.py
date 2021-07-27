# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.
import asyncio
import logging
import typing as t

from aiohttp import (
    web,
)

from minos.api_gateway.common import (
    MinosConfig,
    RESTService,
)

logger = logging.getLogger(__name__)


class DiscoveryService(RESTService):
    """Discovery Service class."""

    def __init__(
        self,
        config: MinosConfig,
        app: web.Application = web.Application(),
        graceful_stop_timeout: int = 5,
        **kwargs: t.Any,
    ):
        super().__init__(
            address=config.discovery.connection.host,
            port=config.discovery.connection.port,
            endpoints=config.discovery.endpoints,
            config=config,
            app=app,
            **kwargs,
        )
        self.graceful_stop_timeout = graceful_stop_timeout

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

# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.
import asyncio
import functools
import logging
from pathlib import Path
from typing import (
    Any,
    Optional,
)

from aiohttp import web

from minos.api_gateway.common import (
    MinosConfig,
    RESTService,
)

from .handlers import DiscoveryHandlers

logger = logging.getLogger(__name__)


class DiscoveryService(RESTService):
    """Discovery Service class."""

    def __init__(
        self, config: MinosConfig, app: Optional[web.Application] = None, graceful_stop_timeout: int = 5, **kwargs: Any,
    ):
        if app is None:
            app = web.Application()

        endpoints = [
            web.get("/discover", functools.partial(DiscoveryHandlers.discover, config=config)),
            web.post("/subscriptions", functools.partial(DiscoveryHandlers.subscribe, config=config)),
            web.delete("/subscriptions", functools.partial(DiscoveryHandlers.unsubscribe, config=config)),
            web.get("/system/health", functools.partial(DiscoveryHandlers.system_health, config=config)),
        ]

        super().__init__(
            address=config.discovery.connection.host,
            port=config.discovery.connection.port,
            endpoints=endpoints,
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

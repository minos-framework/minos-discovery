"""minos.api_gateway.discovery.health_status.checkers module."""

import logging
from asyncio import (
    TimeoutError,
    gather,
)
from typing import (
    Any,
    NoReturn,
)

from aiohttp import (
    ClientConnectorError,
    ClientSession,
    ClientTimeout,
)
from yarl import (
    URL,
)

from minos.api_gateway.common import (
    MinosConfig,
)

from ..database import (
    MinosRedisClient,
)
from ..domain.microservice import (
    MICROSERVICE_KEY_PREFIX,
)

logger = logging.getLogger(__name__)


class HealthStatusChecker:
    """Health Status Checker class."""

    def __init__(self, config: MinosConfig, timeout: float = 5.0):
        self.redis = MinosRedisClient(config=config)
        self.timeout = timeout

    async def check(self) -> NoReturn:
        """Check the health status of the already known microservices.

        :return: This method does not return anything.
        """
        coroutines = []

        async for key in self.redis.redis.scan_iter(match=f"{MICROSERVICE_KEY_PREFIX}:*"):
            coroutines.append(self._check_one(key.decode("utf-8")))

        coroutines = tuple(coroutines)
        await gather(*coroutines)

    async def _check_one(self, key: str):
        logger.info(f"Checking {key!r} health status...")
        try:
            # noinspection PyTypeChecker
            data: dict[str, Any] = await self.redis.get_data(key)
            alive = await self._query_health_status(**data)
            await self._update_one(alive, key, data)
        except Exception as exc:
            logger.warning(f"An exception was raised while checking {key!r}: {exc!r}")

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    async def _query_health_status(self, address: str, port: int, **kwargs) -> bool:
        url = URL.build(scheme="http", host=address, port=port, path="/system/health")

        try:
            async with ClientSession(timeout=ClientTimeout(total=self.timeout)) as session:
                async with session.get(url=url) as response:
                    return response.ok
        except (ClientConnectorError, TimeoutError):
            return False

    async def _update_one(self, alive: bool, key: str, data: dict[str, Any]) -> NoReturn:
        if alive == data["status"]:
            return

        data["status"] = alive
        await self.redis.set_data(key, data)

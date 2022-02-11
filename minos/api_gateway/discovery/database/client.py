"""API Router is responsible for obtaining the connection values for each domain name.

This module obtains the IP, port and status of a microservice. Using the domain name,
it performs a Redis lookup by key value. The value is stored in Redis as JSON.

    Typical usage example:

        class OrdersMinosApiRouter(MinosApiRouter):
            pass

        foo = OrdersMinosApiRouter('order')
        bar = foo.conn_values()
"""

import json
import logging
from typing import (
    Any,
)

import aioredis

from minos.api_gateway.common import (
    MinosConfig,
)
from minos.api_gateway.discovery.domain.microservice import (
    MICROSERVICE_KEY_PREFIX,
)

log = logging.getLogger(__name__)


class MinosRedisClient:
    """Class that connects to Redis and returns the configuration values according to domain name.

    The connection to Redis is made via the environment variables: REDIS_HOST, REDIS_PORT, REDIS_PASSWORD.

    Attributes:
        domain: A string which specifies the Domain Name. Example: order, cart, customer ....
    """

    __slots__ = "address", "port", "password", "redis"

    def __init__(self, config: MinosConfig, pool_size: int = 50):
        """Perform initial configuration and connection to Redis"""

        address = config.discovery.database.host
        port = config.discovery.database.port
        password = config.discovery.database.password

        pool = aioredis.ConnectionPool.from_url(
            f"redis://{address}:{port}", password=password, max_connections=pool_size
        )
        self.redis = aioredis.Redis(connection_pool=pool)

    async def get_data(self, key: str) -> str:
        """Get redis value by key"""
        json_data = {}
        try:
            redis_data = await self.redis.get(key)
            json_data = json.loads(redis_data)
        except Exception:
            pass

        return json_data

    async def get_all(self) -> list:
        """Get redis value by key"""
        data = list()
        try:
            async for key in self.redis.scan_iter(match=f"{MICROSERVICE_KEY_PREFIX}:*"):
                decoded_key = key.decode("utf-8")
                redis_data: dict[str, Any] = await self.redis.get(decoded_key)
                data.append(json.loads(redis_data))
        except Exception:
            pass

        return data

    async def set_data(self, key: str, data: dict):
        async with self.redis as r:
            await r.set(key, json.dumps(data))
            await r.save()

    async def update_data(self):  # pragma: no cover
        """Update specific value"""
        pass

    async def delete_data(self, key: str):
        deleted_elements = await self.redis.delete(key)

        if deleted_elements > 0:
            return True
        else:
            return False

    def get_redis_connection(self):
        """Redis connection itself"""
        return self.redis

    async def flush_db(self):
        await self.redis.flushdb()

    async def ping(self):
        return await self.redis.ping()

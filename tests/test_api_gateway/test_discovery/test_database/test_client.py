import os
from unittest import (
    IsolatedAsyncioTestCase,
)
from unittest.mock import (
    patch,
)
from redis import (
    ConnectionError,
)
from minos.api_gateway.common import (
    MinosConfig,
)
from minos.api_gateway.discovery import (
    MinosRedisClient,
)
from tests.utils import (
    BASE_PATH,
)


class TestDiscoveryHandler(IsolatedAsyncioTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "config.yml"

    def setUp(self) -> None:
        config = MinosConfig(self.CONFIG_FILE_PATH)
        self.redis_client = MinosRedisClient(config=config)

    async def test_redis_wrong_client_connection(self):
        with patch.dict(
            os.environ,
            {
                "DISCOVERY_SERVICE_DB_HOST": "redishost",
                "DISCOVERY_SERVICE_DB_PORT": "8393",
                "DISCOVERY_SERVICE_DB_PASSWORD": "SomePass",
            },
            clear=True,
        ):
            config = MinosConfig(self.CONFIG_FILE_PATH)
            with self.assertRaises(ConnectionError):
                redis_client = MinosRedisClient(config=config)
                await redis_client.ping()

    async def test_redis_client_get_data(self):
        data = await self.redis_client.get_data("a")
        self.assertEqual(data, {})

    async def test_redis_client_set_data(self):
        response = await self.redis_client.set_data("endpoint_name", {"test": "a"})
        self.assertIsNone(response)

    async def test_redis_client_delete_unexisting_data(self):
        response = await self.redis_client.delete_data("nokey")
        self.assertFalse(response)

    async def test_redis_client_delete_data(self):
        await self.redis_client.set_data("endpoint_name", {"test": "a"})
        response = await self.redis_client.delete_data("endpoint_name")
        self.assertTrue(response)

    async def test_redis_client_update_data(self):
        d = {"test": "a"}
        res1 = await self.redis_client.set_data("update_example", d)
        self.assertIsNone(res1)
        await self.redis_client.set_data("update_example", {"test": "b"})
        data = await self.redis_client.get_data("update_example")
        self.assertDictEqual({"test": "b"}, data)

    async def test_redis_client_get_connection(self):
        redis_conn = self.redis_client.get_redis_connection()
        self.assertEqual(type(redis_conn).__name__, "Redis")


import os
import unittest
from unittest import (
    mock,
)
from minos.api_gateway.discovery import MinosRedisClient
from minos.api_gateway.common import (
    MinosConfig,
)
from tests.utils import (
    BASE_PATH,
)


class TestDiscoveryHandler(unittest.TestCase):
    CONFIG_FILE_PATH = BASE_PATH / "test_config.yml"

    @mock.patch.dict(os.environ, {"DISCOVERY_SERVICE_DB_HOST": "redishost"})
    @mock.patch.dict(os.environ, {"DISCOVERY_SERVICE_DB_PORT": "8393"})
    @mock.patch.dict(os.environ, {"DISCOVERY_SERVICE_DB_PASSWORD": "SomePass"})
    def test_redis_client_connection(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        with self.assertRaises(Exception):
            redis_cli = MinosRedisClient(config=config)
            print(redis_cli.get_redis_connection())

    def test_redis_client_get_data(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        redis_cli = MinosRedisClient(config=config)

        data = redis_cli.get_data("a")
        self.assertEquals(data, {})

    def test_redis_client_set_data(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        redis_cli = MinosRedisClient(config=config)

        response = redis_cli.set_data("test_endpoint", {"test": "a"})
        self.assertTrue(response)

    def test_redis_client_delete_unexisting_data(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        redis_cli = MinosRedisClient(config=config)

        response = redis_cli.delete_data("nokey")
        self.assertFalse(response)

    def test_redis_client_delete_data(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        redis_cli = MinosRedisClient(config=config)

        response = redis_cli.delete_data("test_endpoint")
        self.assertTrue(response)

    def test_redis_client_get_connection(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        redis_cli = MinosRedisClient(config=config)

        redis_conn = redis_cli.get_redis_connection()
        self.assertEquals(type(redis_conn).__name__, 'Redis')

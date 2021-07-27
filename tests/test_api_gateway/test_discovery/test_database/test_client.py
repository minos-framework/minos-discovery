import os
import unittest
from unittest import (
    mock,
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


class TestDiscoveryHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.config_file_path = BASE_PATH / "config.yml"
        config = MinosConfig(self.config_file_path)
        self.redis_client = MinosRedisClient(config=config)

    @mock.patch.dict(os.environ, {"DISCOVERY_SERVICE_DB_HOST": "redishost"})
    @mock.patch.dict(os.environ, {"DISCOVERY_SERVICE_DB_PORT": "8393"})
    @mock.patch.dict(os.environ, {"DISCOVERY_SERVICE_DB_PASSWORD": "SomePass"})
    def test_redis_client_connection(self):
        config = MinosConfig(self.config_file_path)
        with self.assertRaises(Exception):
            self.redis_client = MinosRedisClient(config=config)
            print(self.redis_client.get_redis_connection())

    def test_redis_client_get_data(self):
        data = self.redis_client.get_data("a")
        self.assertEqual(data, {})

    def test_redis_client_set_data(self):
        response = self.redis_client.set_data("endpoint_name", {"test": "a"})
        self.assertTrue(response)

    def test_redis_client_delete_unexisting_data(self):
        response = self.redis_client.delete_data("nokey")
        self.assertFalse(response)

    def test_redis_client_delete_data(self):
        response = self.redis_client.set_data("endpoint_name", {"test": "a"})
        self.assertTrue(response)
        response = self.redis_client.delete_data("endpoint_name")
        self.assertTrue(response)

    def test_redis_client_get_connection(self):
        redis_conn = self.redis_client.get_redis_connection()
        self.assertEqual(type(redis_conn).__name__, "Redis")

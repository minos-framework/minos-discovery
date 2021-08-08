import asyncio
import json

from aiohttp.test_utils import (
    AioHTTPTestCase,
    unittest_run_loop
)
from minos.api_gateway.common import (
    MinosConfig,
)

from minos.api_gateway.discovery import DiscoveryService
from tests.utils import BASE_PATH


class TestMicroserviceEndpoints(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryService(
            address=config.discovery.connection.host, port=config.discovery.connection.port, config=config
        )

        return await service.create_application()

    @unittest_run_loop
    async def test_post(self):
        name = "test_name"
        body = {
            "address": "1.1.1.1",
            "port": 1,
            "endpoints": ["test_endpoint_1", "test_endpoint_2"]
        }

        response = await self.client.post(f"/microservices/{name}", json=body)

        self.assertEqual(201, response.status)

    @unittest_run_loop
    async def test_post_missing_param(self):
        name = "test_name"
        body = {
            "port": 1,
            "endpoints": ["test_endpoint_1", "test_endpoint_2"]
        }

        response = await self.client.post(f"/microservices/{name}", json=body)

        self.assertEqual(400, response.status)
        self.assertIn("address", await response.text())

    @unittest_run_loop
    async def test_post_missing_name(self):
        response = await self.client.post("/microservices/")

        self.assertEqual(404, response.status)

    @unittest_run_loop
    async def test_post_empty_body(self):
        name = "test_name"

        response = await self.client.post(f"/microservices/{name}")

        self.assertEqual(400, response.status)

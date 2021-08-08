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
    async def test_get(self):
        name = "test_name"
        endpoint_name = "test_endpoint_1"
        body = {
            "address": "1.1.1.1",
            "port": 1,
            "endpoints": [endpoint_name]
        }

        await self.client.post(f"/microservices/{name}", json=body)

        response = await self.client.get(f"/microservices/endpoints/{endpoint_name}")

        self.assertEqual(200, response.status)

        body = await response.json()

        self.assertEqual("1.1.1.1", body["address"])
        self.assertEqual(1, int(body["port"]))
        self.assertEqual("test_name", body["name"])

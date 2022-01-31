from aiohttp.test_utils import (
    AioHTTPTestCase,
)

from minos.api_gateway.common import (
    MinosConfig,
)
from minos.api_gateway.discovery import (
    DiscoveryService,
)
from tests.utils import (
    BASE_PATH,
)


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

    async def test_get(self):
        response = await self.client.get("/endpoints")

        self.assertEqual(200, response.status)
        self.assertIsInstance(await response.json(), list)

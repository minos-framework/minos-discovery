from aiohttp.test_utils import (
    AioHTTPTestCase,
    unittest_run_loop,
)
import typing as t
from minos.api_gateway.common import (
    MinosConfig,
)
from tests.utils import (
    BASE_PATH,
)
from aiohttp import (
    web,
)
from minos.api_gateway.discovery import (
    DiscoveryService
)


class TestDiscoveryService(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "test_config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        config = MinosConfig(self.CONFIG_FILE_PATH)
        rest_interface = DiscoveryService(config=config)

        return await rest_interface.create_application()

    @unittest_run_loop
    async def test_discover(self):
        url = "/discover"
        resp = await self.client.request("GET", url)
        assert resp.status == 200
        text = await resp.text()
        assert "discover" in text

        url = "/subscribe"
        resp = await self.client.request("POST", url)
        assert resp.status == 200
        text = await resp.text()
        assert "subscribe" in text

        url = "/unsubscribe"
        resp = await self.client.request("POST", url)
        assert resp.status == 200
        text = await resp.text()
        assert "unsubscribe" in text

        url = "/system/health"
        resp = await self.client.request("GET", url)
        assert resp.status == 200



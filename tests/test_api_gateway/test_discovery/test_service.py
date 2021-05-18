from aiohttp import (
    web,
)
from aiohttp.test_utils import (
    AioHTTPTestCase,
    unittest_run_loop,
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


class TestDiscoveryService(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "test_config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        app = web.Application()
        config = MinosConfig(self.CONFIG_FILE_PATH)
        rest_interface = DiscoveryService(config=config, app=app)

        return await rest_interface.create_application()

    @unittest_run_loop
    async def test_discover(self):
        url = "/discover"
        resp = await self.client.request("GET", url)
        assert resp.status == 200
        text = await resp.text()
        assert "discover" in text

    @unittest_run_loop
    async def test_subscribe(self):
        url = "/subscribe"
        resp = await self.client.request("POST", url)
        assert resp.status == 200
        text = await resp.text()
        assert "subscribe" in text

    @unittest_run_loop
    async def test_unsubscribe(self):
        url = "/unsubscribe"
        resp = await self.client.request("POST", url)
        assert resp.status == 200
        text = await resp.text()
        assert "unsubscribe" in text

    @unittest_run_loop
    async def test_system_health(self):
        url = "/system/health"
        resp = await self.client.request("GET", url)
        assert resp.status == 200

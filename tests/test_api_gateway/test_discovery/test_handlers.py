from aiohttp import web
from aiohttp.test_utils import (
    AioHTTPTestCase,
    unittest_run_loop,
)

from minos.api_gateway.common import MinosConfig
from minos.api_gateway.discovery import (
    DiscoveryService,
    handlers,
)
from tests.utils import BASE_PATH


# TODO Redo these tests without AioHTTPTestCase
class TestDiscoveryHandler(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryService(config=config)

        return await service.create_application()

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

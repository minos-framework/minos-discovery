import json

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
    CONFIG_FILE_PATH = BASE_PATH / "config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        app = web.Application()
        config = MinosConfig(self.CONFIG_FILE_PATH)
        rest_interface = DiscoveryService(config=config, app=app)

        return await rest_interface.create_application()

    @unittest_run_loop
    async def test_subscribe(self):
        url = "/subscribe"
        resp = await self.client.request(
            "POST", url, data=json.dumps(dict(ip="127.0.0.1", port=5000, name="test_endpoint"))
        )
        assert resp.status == 200
        text = await resp.text()
        assert "Service added" in text

    @unittest_run_loop
    async def test_discover(self):
        url = "/subscribe"
        resp = await self.client.request(
            "POST", url, data=json.dumps(dict(ip="127.0.0.1", port=5000, name="test_endpoint"))
        )
        assert resp.status == 200
        text = await resp.text()
        assert "Service added" in text

        url = "/discover?name=test_endpoint"
        resp = await self.client.request("GET", url)
        assert resp.status == 200
        text = await resp.text()
        result = json.loads(text)
        self.assertDictEqual(
            {"ip": "127.0.0.1", "port": 5000, "name": "test_endpoint", "status": True, "subscribed": True}, result
        )

    @unittest_run_loop
    async def test_discover_no_name(self):
        url = "/subscribe"
        resp = await self.client.request(
            "POST", url, data=json.dumps(dict(ip="127.0.0.1", port=5000, name="test_endpoint"))
        )
        assert resp.status == 200
        text = await resp.text()
        assert "Service added" in text

        url = "/discover"
        resp = await self.client.request("GET", url)
        assert resp.status == 400
        text = await resp.text()
        assert "not found." in text

    @unittest_run_loop
    async def test_unsubscribe(self):
        url = "/unsubscribe?name=test_endpoint"
        resp = await self.client.request("POST", url)
        assert resp.status == 200
        text = await resp.text()
        assert "Unsubscription done!" in text

    @unittest_run_loop
    async def test_unsubscribe_no_name(self):
        url = "/unsubscribe"
        resp = await self.client.request("POST", url)
        assert resp.status == 400
        text = await resp.text()
        assert "not found." in text

    @unittest_run_loop
    async def test_system_health(self):
        url = "/system/health"
        resp = await self.client.request("GET", url)
        assert resp.status == 200

    @unittest_run_loop
    async def test_wrong_parameter_ip(self):
        url = "/subscribe"
        resp = await self.client.request("POST", url, data=json.dumps(dict(port=5000, name="test_endpoint")))
        assert resp.status == 400
        text = await resp.text()
        assert "ip not found" in text

    @unittest_run_loop
    async def test_wrong_parameter_name(self):
        url = "/subscribe"
        resp = await self.client.request("POST", url, data=json.dumps(dict(ip="127.0.0.1", port=5000)))
        assert resp.status == 400
        text = await resp.text()
        assert "name not found" in text

    @unittest_run_loop
    async def test_no_port(self):
        url = "/subscribe"
        resp = await self.client.request("POST", url, data=json.dumps(dict(ip="127.0.0.1", name="test_endpoint")))
        assert resp.status == 200
        text = await resp.text()
        assert "Service added" in text

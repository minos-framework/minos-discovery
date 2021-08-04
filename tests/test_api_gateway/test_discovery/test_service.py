import json
import unittest
from unittest.mock import (
    call,
    patch,
)

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


class TestDiscoveryService(unittest.IsolatedAsyncioTestCase):
    def test_default_graceful_stop_timeout(self):
        app = web.Application()
        service = DiscoveryService(app=app)

        self.assertEqual(5, service.graceful_stop_timeout)

    async def test_stop(self):
        app = web.Application()
        service = DiscoveryService(app=app)

        with patch("asyncio.sleep") as mock:
            mock.return_value = None
            await service.stop()
            self.assertEqual(1, mock.call_count)
            self.assertEqual(call(service.graceful_stop_timeout), mock.call_args)


class TestDiscoveryServiceEndpoints(AioHTTPTestCase):
    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        app = web.Application()
        service = DiscoveryService(app=app)

        return await service.create_application()

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


if __name__ == "__main__":
    unittest.main()

"""tests.test_api_gateway.test_discovery.test_periodic.test_abc module."""

import unittest

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
    HealthStatusChecker,
    MinosRedisClient,
)
from tests.utils import (
    BASE_PATH,
)


class TestRestInterfaceService(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "config.yml"

    def setUp(self) -> None:
        super().setUp()
        self.config = MinosConfig(self.CONFIG_FILE_PATH)
        self.redis = MinosRedisClient(config=self.config)
        self.redis.flush_db()

    def tearDown(self) -> None:
        self.redis.flush_db()
        super().tearDown()

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """

        async def system_health(request):
            return web.json_response(data="")

        app = web.Application()
        app.router.add_get("/system/health", system_health)
        return app

    @unittest_run_loop
    async def test_existing_endpoint(self):
        # Create endpoint
        endpoint_data = dict(address=self.client.host, port=self.client.port, status=True)
        await self.redis.set_data("microservice:system_health", endpoint_data)

        checker = HealthStatusChecker(config=self.config)
        await checker.check()

        data = await self.redis.get_data("microservice:system_health")

        self.assertEqual(endpoint_data, data)

    @unittest_run_loop
    async def test_existing_endpoint_modify_to_true(self):
        # Create endpoint
        expected = dict(address=self.client.host, port=self.client.port, status=False)
        await self.redis.set_data("microservice:system_health2", expected)
        expected["status"] = True

        checker = HealthStatusChecker(config=self.config)
        await checker.check()

        observed = await self.redis.get_data("microservice:system_health2")
        self.assertEqual(expected, observed)

    @unittest_run_loop
    async def test_unexisting_endpoint(self):
        # Create endpoint
        await self.redis.set_data(
            "microservice:system_health_wrong", dict(address=self.client.host, port=5050, status=False)
        )

        checker = HealthStatusChecker(config=self.config)
        await checker.check()

        observed = await self.redis.get_data("microservice:system_health_wrong")

        expected = dict(address=self.client.host, port=5050, status=False)
        self.assertEqual(expected, observed)

    @unittest_run_loop
    async def test_check_not_raises(self):
        # Create endpoint
        await self.redis.set_data("foo", {"address": "bad"})

        checker = HealthStatusChecker(config=self.config)
        await checker.check()
        self.assertEqual({"address": "bad"}, await self.redis.get_data("foo"))


if __name__ == "__main__":
    unittest.main()

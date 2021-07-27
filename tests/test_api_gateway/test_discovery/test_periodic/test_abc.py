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
        endpoint_data = dict(
            ip=self.client.host, port=self.client.port, name="system_health", status=True, subscribed=True
        )
        self.redis.set_data("system_health", endpoint_data)

        checker = HealthStatusChecker(config=self.config)
        await checker.check()

        data = self.redis.get_data("system_health")

        self.assertEqual(data, endpoint_data)

    @unittest_run_loop
    async def test_existing_endpoint_modify_to_true(self):
        # Create endpoint
        endpoint_data = dict(
            ip=self.client.host, port=self.client.port, name="system_health2", status=False, subscribed=True
        )
        self.redis.set_data("system_health2", endpoint_data)

        checker = HealthStatusChecker(config=self.config)
        await checker.check()

        data = self.redis.get_data("system_health2")
        endpoint_data["status"] = True
        self.assertEqual(data, endpoint_data)

    @unittest_run_loop
    async def test_unexisting_endpoint(self):
        # Create endpoint
        self.redis.set_data(
            "system_health_wrong",
            dict(ip=self.client.host, port=5050, name="system_health_wrong", status=True, subscribed=True),
        )

        checker = HealthStatusChecker(config=self.config)
        await checker.check()

        data = self.redis.get_data("system_health_wrong")

        self.assertEqual(
            data, dict(ip=self.client.host, port=5050, name="system_health_wrong", status=False, subscribed=True)
        )

    @unittest_run_loop
    async def test_check_not_raises(self):
        # Create endpoint
        self.redis.set_data("foo", {"ip": "bad"})

        checker = HealthStatusChecker(config=self.config)
        await checker.check()
        self.assertEqual({}, self.redis.get_data("foo"))


if __name__ == "__main__":
    unittest.main()

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
        config = MinosConfig(self.CONFIG_FILE_PATH)

        # Delete all REDIS DB
        redis = MinosRedisClient(config=config)
        redis.flush_db()

        # Create endpoint
        endpoint_data = dict(
            ip=self.client.host, port=self.client.port, name="system_health", status=True, subscribed=True
        )
        redis.set_data("system_health", endpoint_data)

        mhc = HealthStatusChecker(config=config)
        await mhc.check()

        data = redis.get_data("system_health")

        self.assertDictEqual(data, endpoint_data)

    @unittest_run_loop
    async def test_existing_endpoint_modify_to_true(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)

        # Delete all REDIS DB
        redis = MinosRedisClient(config=config)
        redis.flush_db()

        # Create endpoint
        endpoint_data = dict(
            ip=self.client.host, port=self.client.port, name="system_health2", status=False, subscribed=True
        )
        redis.set_data("system_health2", endpoint_data)

        mhc = HealthStatusChecker(config=config)
        await mhc.check()

        data = redis.get_data("system_health2")
        endpoint_data["status"] = True
        self.assertDictEqual(data, endpoint_data)

    @unittest_run_loop
    async def test_unexisting_endpoint(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)

        # Delete all REDIS DB
        redis = MinosRedisClient(config=config)
        redis.flush_db()

        # Create endpoint
        redis.set_data(
            "system_health_wrong",
            dict(ip=self.client.host, port=5050, name="system_health_wrong", status=True, subscribed=True),
        )

        mhc = HealthStatusChecker(config=config)
        await mhc.check()

        data = redis.get_data("system_health_wrong")

        self.assertDictEqual(
            data, dict(ip=self.client.host, port=5050, name="system_health_wrong", status=False, subscribed=True)
        )

import json
import unittest
from unittest.mock import (
    call,
    patch,
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
    CONFIG_FILE_PATH = BASE_PATH / "config.yml"

    def test_default_graceful_stop_timeout(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryService(
            address=config.discovery.connection.host, port=config.discovery.connection.port, config=config
        )

        self.assertEqual(5, service.graceful_stop_timeout)

    async def test_stop(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryService(
            address=config.discovery.connection.host, port=config.discovery.connection.port, config=config
        )

        with patch("asyncio.sleep") as mock:
            mock.return_value = None
            await service.stop()
            self.assertEqual(1, mock.call_count)
            self.assertEqual(call(service.graceful_stop_timeout), mock.call_args)


if __name__ == "__main__":
    unittest.main()

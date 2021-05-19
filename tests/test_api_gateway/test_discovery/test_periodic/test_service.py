"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
import unittest
from unittest.mock import (
    MagicMock,
)

from aiomisc.service.periodic import (
    PeriodicService,
)

from minos.api_gateway.common import (
    MinosConfig,
)
from minos.api_gateway.discovery import (
    DiscoveryPeriodicHealthChecker,
)
from tests.utils import (
    BASE_PATH,
)


class TestMinosQueueService(unittest.TestCase):
    CONFIG_FILE_PATH = BASE_PATH / "test_config.yml"

    def test_is_instance(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryPeriodicHealthChecker(interval=0.1, config=config)
        self.assertIsInstance(service, PeriodicService)

    async def test_start(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryPeriodicHealthChecker(interval=0.1, loop=None, config=config)
        service.start = MagicMock(side_effect=service.start)
        await service.start()
        self.assertEqual(1, service.start.call_count)

    async def test_callback(self):
        config = MinosConfig(self.CONFIG_FILE_PATH)
        service = DiscoveryPeriodicHealthChecker(interval=0.1, loop=None, config=config)
        service.status_checker.perform_health_check = MagicMock(side_effect=service.status_checker.perform_health_check)
        await service.callback()
        self.assertEqual(1, service.status_checker.perform_health_check.call_count)


if __name__ == "__main__":
    unittest.main()

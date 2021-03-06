import unittest
from unittest.mock import (
    PropertyMock,
    patch,
)

from typer.testing import (
    CliRunner,
)

from minos.api_gateway.discovery.cli import (
    EntrypointLauncher,
)
from tests.utils import (
    FakeEntrypoint,
    FakeLoop,
)

runner = CliRunner()


class Foo:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class TestCli(unittest.TestCase):
    def setUp(self):
        self.services = ("a", "b", Foo)
        self.launcher = EntrypointLauncher(services=self.services)

    def test_launch(self):
        loop = FakeLoop()
        entrypoint = FakeEntrypoint()
        with patch("minos.api_gateway.discovery.EntrypointLauncher.loop", new_callable=PropertyMock) as mock_loop:
            mock_loop.return_value = loop

            with patch("minos.api_gateway.discovery.EntrypointLauncher.entrypoint", new_callable=PropertyMock) as mock:
                mock.return_value = entrypoint
                self.launcher.launch()
            self.assertEqual(1, entrypoint.graceful_shutdown_call_count)
            self.assertEqual(1, loop.call_count)

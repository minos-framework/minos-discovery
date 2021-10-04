from pathlib import (
    Path,
)

BASE_PATH = Path(__file__).parent


class FakeEntrypoint:
    """For testing purposes."""

    def __init__(self):
        self.graceful_shutdown_call_count = 0

    async def __aenter__(self):
        """For testing purposes."""

    def graceful_shutdown(self, *args, **kwargs):
        """For testing purposes."""
        self.graceful_shutdown_call_count += 1


class FakeLoop:
    """For testing purposes."""

    def __init__(self):
        self.call_count = 0

    def run_forever(self):
        """For testing purposes."""
        self.call_count += 1

    def run_until_complete(self, *args, **kwargs):
        """For testing purposes."""

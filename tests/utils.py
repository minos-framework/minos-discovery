"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from pathlib import (
    Path,
)

BASE_PATH = Path(__file__).parent


class FakeEntrypoint:
    """For testing purposes."""

    def __init__(self):
        self.call_count = 0
        self.graceful_shutdown_call_count = 0

    def __enter__(self):
        self.call_count += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

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

import logging
from asyncio import (
    AbstractEventLoop,
)
from typing import (
    NoReturn,
)

from aiomisc.entrypoint import (
    Entrypoint,
)
from aiomisc.utils import (
    create_default_event_loop,
)
from cached_property import (
    cached_property,
)

logger = logging.getLogger(__name__)


class EntrypointLauncher:
    """EntryPoint Launcher class."""

    def __init__(self, services: tuple):
        self.services = services

    def launch(self) -> NoReturn:
        """Launch a new execution and keeps running forever..

        :return: This method does not return anything.
        """
        logger.info("Starting Discovery...")
        try:
            self.loop.run_until_complete(self.entrypoint.__aenter__())
            logger.info("Discovery is up and running!")
            self.loop.run_forever()
        except KeyboardInterrupt:  # pragma: no cover
            logger.info("Stopping discovery...")
        finally:
            self.graceful_shutdown()

    def graceful_shutdown(self, err: Exception = None) -> None:
        """Shutdown the services execution gracefully.

        :return: This method does not return anything.
        """
        self.loop.run_until_complete(self.entrypoint.graceful_shutdown(err))

    @cached_property
    def entrypoint(self) -> Entrypoint:
        """Entrypoint instance.

        :return: An ``Entrypoint`` instance.
        """

        return Entrypoint(*self.services, loop=self.loop)  # pragma: no cover

    @cached_property
    def loop(self) -> AbstractEventLoop:
        """Create the loop.

        :return: An ``AbstractEventLoop`` instance.
        """
        return create_default_event_loop()[0]  # pragma: no cover

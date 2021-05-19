# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

import typing as t

from aiohttp import (
    web,
)

from minos.api_gateway.common import (
    MinosConfig,
    RESTService,
)


class DiscoveryService(RESTService):
    def __init__(self, config: MinosConfig, app: web.Application = web.Application(), **kwds: t.Any):
        super().__init__(
            address=config.discovery.connection.host,
            port=config.discovery.connection.port,
            endpoints=config.discovery.endpoints,
            config=config,
            app=app,
            **kwds
        )

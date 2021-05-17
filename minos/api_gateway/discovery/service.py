# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

import typing as t
from minos.api_gateway.common import (
    RESTService,
    MinosConfig
)


class DiscoveryService(RESTService):
    def __init__(self, config: MinosConfig, **kwds: t.Any):
        super().__init__(address=config.discovery.connection.host, port=config.discovery.connection.port, endpoints=config.discovery.endpoints, **kwds)

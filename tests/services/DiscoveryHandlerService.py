from aiohttp import (
    web,
)

from minos.api_gateway.common import (
    MinosConfig,
)


class DiscoveryHandlers(object):
    async def discover(self, request, config: MinosConfig, **kwargs):
        return web.Response(text="discover")

    async def subscribe(self, request, config: MinosConfig, **kwargs):
        return web.Response(text="subscribe")

    async def unsubscribe(self, request, config: MinosConfig, **kwargs):
        return web.Response(text="unsubscribe")

    async def system_health(self, request, config: MinosConfig, **kwargs):
        return web.json_response({"host": request.host}, status=200)

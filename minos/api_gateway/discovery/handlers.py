from aiohttp import web


class DiscoveryHandlers(object):
    async def discover(self, request):
        return web.Response(text="discover")

    async def subscribe(self, request):
        return web.Response(text="subscribe")

    async def unsubscribe(self, request):
        return web.Response(text="unsubscribe")

    async def system_health(self, request):
        return web.json_response({"host": request.host}, status=200)

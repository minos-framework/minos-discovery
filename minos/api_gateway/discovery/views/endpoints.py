from aiohttp import (
    web,
)

from ..domain import (
    Microservice,
)
from .router import (
    routes,
)


@routes.view("/endpoints")
class EndpointsView(web.View):
    async def get(self):
        redis_client = self.request.app["db_client"]
        endpoints = await Microservice.get_all(redis_client)

        return web.json_response(endpoints)

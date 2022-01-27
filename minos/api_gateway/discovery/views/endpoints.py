from aiohttp import (
    web,
)

from ..domain import (
    Microservice,
)
from ..exceptions import (
    NotFoundException,
)
from .router import (
    routes,
)


@routes.view("/endpoints")
class EndpointsView(web.View):
    async def get(self):
        redis_client = self.request.app["db_client"]

        try:
            endpoints = await Microservice.get_all(redis_client)
        except NotFoundException:
            return web.HTTPNotFound()

        return web.json_response(endpoints)

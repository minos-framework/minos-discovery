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


@routes.view("/microservices/endpoints/{name}")
class EndpointView(web.View):
    async def get(self):
        name = self.request.match_info["name"]

        redis_client = self.request.app["db_client"]

        try:
            microservice = await Microservice.find_by_endpoint(name, redis_client)
        except NotFoundException:
            return web.HTTPNoContent()

        return web.json_response(microservice.__dict__)

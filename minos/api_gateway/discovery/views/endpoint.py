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


@routes.view("/microservices")
class EndpointView(web.View):
    async def get(self):
        url = self.request.query["url"]
        if not url:
            raise web.HTTPBadRequest(text="Missing 'url' query param")

        redis_client = self.request.app["db_client"]

        try:
            microservice = await Microservice.find_by_endpoint(url, redis_client)
        except NotFoundException:
            return web.HTTPNoContent()

        return web.json_response(microservice.__dict__)

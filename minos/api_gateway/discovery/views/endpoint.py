from aiohttp import (
    web,
)

from ..domain import (
    Microservice,
)
from ..domain.endpoint import (
    ConcreteEndpoint,
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
        try:
            verb = self.request.query["verb"]
            path = self.request.query["path"]
        except KeyError:
            raise web.HTTPBadRequest(text="Missing either 'verb' or 'path' query params")

        redis_client = self.request.app["db_client"]

        endpoint = ConcreteEndpoint(verb, path)
        try:
            microservice = await Microservice.find_by_endpoint(endpoint, redis_client)
        except NotFoundException:
            return web.HTTPNoContent()

        return web.json_response(microservice.__dict__)

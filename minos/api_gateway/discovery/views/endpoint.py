from aiohttp import (
    web,
)

from ..domain import (
    CannotInstantiateException,
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

        try:
            endpoint = ConcreteEndpoint(verb, path)
        except CannotInstantiateException:
            raise web.HTTPBadRequest(text="The given endpoint cannot have parts enclosed in brackets")

        try:
            microservice = await Microservice.find_by_endpoint(endpoint, redis_client)
        except NotFoundException:
            return web.HTTPNotFound()

        return web.json_response(microservice.to_json())

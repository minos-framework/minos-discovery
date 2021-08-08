import logging
from json import JSONDecodeError

from aiohttp import (
    web
)

from ..domain import (
    Microservice,
)

logger = logging.getLogger(__name__)

routes = web.RouteTableDef()


@routes.view("/microservices/{name}")
class MicroserviceView(web.View):
    async def post(self):
        try:
            body = await self.request.json()
        except JSONDecodeError as exc:
            raise web.HTTPBadRequest(text="Empty or wrong body")
        else:
            body["name"] = self.request.match_info["name"]

        from .. import MinosRedisClient
        redis_client = MinosRedisClient(config=self.request.app["config"])

        try:
            microservice = Microservice(**body)
        except TypeError as exc:
            raise web.HTTPBadRequest(text=exc.args[0])
        microservice.save(redis_client)

        return web.Response()

    async def get(self):
        pass


@routes.view("/endpoints/{endpoint_name}")
class EndpointView(web.View):
    async def post(self):
        pass

    async def get(self):
        pass

    async def delete(self):
        pass

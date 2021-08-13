import logging
from json import (
    JSONDecodeError,
)

from aiohttp import (
    web,
)

from ..domain import (
    Microservice,
)
from .router import (
    routes,
)

logger = logging.getLogger(__name__)


@routes.view("/microservices/{name}")
class MicroserviceView(web.View):
    async def post(self):
        body = await self.get_body()

        redis_client = self.request.app["db_client"]

        try:
            microservice = Microservice(**body)
        except TypeError as exc:
            raise web.HTTPBadRequest(text=exc.args[0])
        await microservice.save(redis_client)

        return web.HTTPCreated()

    async def delete(self):
        microservice_name = self.request.match_info["name"]

        redis_client = self.request.app["db_client"]

        await Microservice.delete(microservice_name, redis_client)

        return web.HTTPOk()

    async def get_body(self):
        try:
            body = await self.request.json()
        except JSONDecodeError:
            raise web.HTTPBadRequest(text="Empty or wrong body")
        else:
            body["name"] = self.request.match_info["name"]

        return body

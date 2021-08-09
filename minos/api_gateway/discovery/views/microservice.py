import logging
from json import (
    JSONDecodeError,
)

from aiohttp import (
    web,
)

from ..database import (
    MinosRedisClient,
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

        redis_client = MinosRedisClient(config=self.request.app["config"])

        try:
            microservice = Microservice(**body)
        except TypeError as exc:
            raise web.HTTPBadRequest(text=exc.args[0])
        await microservice.save(redis_client)

        return web.HTTPCreated()

    async def delete(self):
        body = await self.get_body()

        redis_client = MinosRedisClient(config=self.request.app["config"])

        await Microservice.delete_by_endpoint(body["endpoints"], redis_client)

        return web.HTTPOk()

    async def get_body(self):
        try:
            body = await self.request.json()
        except JSONDecodeError:
            raise web.HTTPBadRequest(text="Empty or wrong body")
        else:
            body["name"] = self.request.match_info["name"]

        return body

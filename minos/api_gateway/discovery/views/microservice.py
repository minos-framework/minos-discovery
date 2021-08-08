import logging
from json import JSONDecodeError

from aiohttp import (
    web
)

from . import routes
from ..database import MinosRedisClient
from ..domain import (
    Microservice,
)

logger = logging.getLogger(__name__)


@routes.view("/microservices/{name}")
class MicroserviceView(web.View):
    async def post(self):
        try:
            body = await self.request.json()
        except JSONDecodeError as exc:
            raise web.HTTPBadRequest(text="Empty or wrong body")
        else:
            body["name"] = self.request.match_info["name"]

        redis_client = MinosRedisClient(config=self.request.app["config"])

        try:
            microservice = Microservice(**body)
        except TypeError as exc:
            raise web.HTTPBadRequest(text=exc.args[0])
        microservice.save(redis_client)

        return web.HTTPCreated()

    async def delete(self):
        pass

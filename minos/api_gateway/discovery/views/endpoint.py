from aiohttp import web

from ..exceptions import NotFoundException
from ..domain import Microservice
from ..views import routes
from ..database import MinosRedisClient


@routes.view("/microservices/endpoints/{name}")
class EndpointView(web.View):
    async def get(self):
        name = self.request.match_info["name"]

        redis_client = MinosRedisClient(config=self.request.app["config"])

        try:
            microservice = Microservice.find_by_endpoint(name, redis_client)
        except NotFoundException:
            return web.HTTPNoContent()

        return web.json_response(microservice.__dict__)

from aiohttp import web

from ..domain import Microservice
from ..views import routes


@routes.view("/microservices/endpoints/{name}")
class EndpointView(web.View):
    async def get(self):
        name = self.request.match_info["name"]

        from .. import MinosRedisClient
        redis_client = MinosRedisClient(config=self.request.app["config"])

        microservice = Microservice.find_by_endpoint(name, redis_client)
        # TODO Add exception if not exists

        return web.json_response(microservice.__dict__)

    async def post(self):
        pass

    async def delete(self):
        pass

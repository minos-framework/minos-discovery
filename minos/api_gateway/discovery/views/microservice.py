import logging
from json import JSONDecodeError
from typing import Any

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
    async def parse(self, microservice_body) -> dict[str, Any]:
        params = ("address", "port", "endpoints")
        missing_params = list()
        for param in params:
            if param not in microservice_body:
                missing_params.append(param)

        if len(missing_params) != 0:
            raise web.HTTPBadRequest(text=f"Missing the following body parameters {missing_params}")

        return microservice_body

    async def post(self):
        try:
            body = await self.request.json()
        except JSONDecodeError as exc:
            raise web.HTTPBadRequest(text="Empty or wrong body")
        else:
            microservice_body = await self.parse(body)

        microservice = Microservice(
            name=self.request.match_info["name"],
            address=microservice_body["address"],
            port=microservice_body["port"],
            endpoints=microservice_body["endpoints"]
        )

        return web.json_response(data="ok")

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

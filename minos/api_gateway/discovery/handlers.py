from aiohttp import (
    web,
)

from .database import (
    MinosRedisClient,
)
from .domain import (
    Microservice,
)

routes = web.RouteTableDef()


@routes.view("/microservices/{name}")
class MicroserviceView(web.View):
    async def post(self):

        microservice = Microservice(
            name=self.request.match_info["name"],
            address=
        )

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


async def validate_input(request: web.Request):
    input_json = await request.json()
    errors = True
    if "ip" not in input_json:
        return web.json_response("Value ip not found.", status=400), errors
    if "name" not in input_json:
        return web.json_response("Value name not found.", status=400), errors

    return None, False


async def get_formatted(request: web.Request) -> dict:
    input_json = await request.json()

    if "port" not in input_json:
        input_json["port"] = None

    return {
        "ip": input_json["ip"],
        "port": input_json["port"],
        "name": input_json["name"],
        "status": True,
        "subscribed": True,
    }


@routes.get("/subscriptions")
async def discover(request: web.Request):
    name = request.query.get("name")
    if not name:
        return web.json_response('Parameter "name" not found.', status=400)

    # Search by key in Redis and return JSON
    redis_cli = MinosRedisClient(config=request.app["config"])

    # Get JSON data
    data = redis_cli.get_data(name)
    return web.json_response(data=data)


@routes.post("/subscriptions")
async def subscribe(request: web.Request):
    validation, errors = await validate_input(request)

    if errors:
        return validation

    input_json = await get_formatted(request)

    redis_client = MinosRedisClient(config=request.app["config"])

    redis_client.set_data(input_json["name"], input_json)

    return web.json_response(text="Service added")


@routes.delete("/subscriptions")
async def unsubscribe(request: web.Request):
    name = request.query.get("name")
    if not name:
        return web.json_response('Parameter "name" not found.', status=400)
    else:
        # Search by key in Redis and set subscription to unsubscribed
        redis_cli = MinosRedisClient(config=request.app["config"])

        # Get JSON data
        data = redis_cli.get_data(name)

        data["subscribed"] = False

        redis_cli.set_data(name, data)

        return web.json_response(text="Unsubscription done!")


@routes.get("/system/health")
async def system_health(request: web.Request):
    return web.json_response({"host": request.host})

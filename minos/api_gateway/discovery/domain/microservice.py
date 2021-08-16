from typing import NoReturn

from ..exceptions import NotFoundException
from .endpoint import (
    ConcreteEndpoint,
    GenericEndpoint,
)

MICROSERVICE_KEY_PREFIX = "microservice"
ENDPOINT_KEY_PREFIX = "endpoint"


class Microservice:
    def __init__(self, name: str, address: str, port: int, endpoints: list[list[str]]):
        self.name = name
        self.address = address
        self.port = port
        self.endpoints: list[GenericEndpoint] = [
            GenericEndpoint(endpoint_verb, endpoint_path) for endpoint_verb, endpoint_path in endpoints
        ]
        self.status = True

    async def save(self, db_client) -> NoReturn:
        microservice_value = {
            "name": self.name,
            "address": self.address,
            "port": self.port,
            "endpoints": [
                f"{ENDPOINT_KEY_PREFIX}:{endpoint.verb}:{endpoint.path_as_str}" for endpoint in self.endpoints
            ],
        }

        microservice_key = f"{MICROSERVICE_KEY_PREFIX}:{self.name}"
        await db_client.set_data(microservice_key, microservice_value)
        for endpoint_key in microservice_value["endpoints"]:
            await db_client.set_data(endpoint_key, microservice_key)

    @classmethod
    async def find_by_endpoint(cls, concrete_endpoint: ConcreteEndpoint, db_client):
        async for key_bytes in db_client.redis.scan_iter(match=f"{ENDPOINT_KEY_PREFIX}:*"):
            _, verb, path = key_bytes.decode("utf-8").split(":")
            endpoint = GenericEndpoint(verb, path)
            if endpoint.matches(concrete_endpoint):
                microservice_key = await db_client.get_data(key_bytes)
                microservice_dict = await db_client.get_data(microservice_key)
                microservice_dict["endpoints"] = [
                    endpoint_key.split(":")[1::-1] for endpoint_key in microservice_dict["endpoints"]
                ]
                return cls(**microservice_dict)

        raise NotFoundException

    @classmethod
    async def delete(cls, microservice_name, redis_client):
        microservice_data = await redis_client.get_data(f"{MICROSERVICE_KEY_PREFIX}:{microservice_name}")
        endpoints = microservice_data["endpoints"]
        await redis_client.delete_data(microservice_name)
        for endpoint in endpoints:
            await redis_client.delete_data(endpoint)

    def to_json(self):
        microservice_dict = {
            "name": self.name,
            "address": self.address,
            "port": self.port,
            "endpoints": [[endpoint.verb, endpoint.path_as_str] for endpoint in self.endpoints],
            "status": self.status,
        }

        return microservice_dict

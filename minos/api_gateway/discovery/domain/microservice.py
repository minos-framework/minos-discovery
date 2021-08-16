from typing import (
    NoReturn,
)

from ..exceptions import (
    NotFoundException,
)
from .endpoint import (
    ConcreteEndpoint,
    GenericEndpoint,
)


class Microservice:
    def __init__(self, name: str, address: str, port: int, endpoints: list[list[str]]):
        self.name = name
        self.address = address
        self.port = port
        self.endpoints: list[GenericEndpoint] = [
            GenericEndpoint(endpoint_verb, endpoint_path) for endpoint_verb, endpoint_path in endpoints
        ]

    async def save(self, db_client) -> NoReturn:
        microservice_value = {"name": self.name, "address": self.address, "port": self.port}

        for endpoint in self.endpoints:
            await db_client.set_data(f"endpoint:{endpoint.verb}:{endpoint.path_as_str}", microservice_value)

    @classmethod
    async def find_by_endpoint(cls, concrete_endpoint: ConcreteEndpoint, db_client):
        async for key_bytes in db_client.redis.scan_iter(match="endpoint:*"):
            _, verb, path = key_bytes.decode("utf-8").split(":")
            endpoint = GenericEndpoint(verb, path)
            if endpoint.matches(concrete_endpoint):
                microservice_dict = await db_client.get_data(key_bytes)
                return cls(**microservice_dict, endpoints=[])

        raise NotFoundException

    @staticmethod
    async def delete_by_endpoint(endpoints: list[str], db_client):
        for endpoint in endpoints:
            await db_client.delete_data(endpoint)

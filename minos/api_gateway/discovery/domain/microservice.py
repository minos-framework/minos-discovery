from typing import (
    NoReturn,
)

from ..exceptions import (
    NotFoundException,
)
from .endpoint import (
    Endpoint,
)


class Microservice:
    def __init__(self, name: str, address: str, port: int, endpoints: list[str]):
        self.name = name
        self.address = address
        self.port = port
        self.endpoints = [Endpoint(endpoint_path) for endpoint_path in endpoints]

    async def save(self, db_client) -> NoReturn:
        microservice_value = {"name": self.name, "address": self.address, "port": self.port}

        for endpoint in self.endpoints:
            await db_client.set_data(endpoint.path, microservice_value)

    @classmethod
    async def find_by_endpoint(cls, url: str, db_client):
        async for key_bytes in db_client.redis.scan_iter():
            key = key_bytes.decode("utf-8")
            endpoint = Endpoint(key)
            if endpoint.matches(url):
                microservice_dict = await db_client.get_data(key)

                return cls(**microservice_dict, endpoints=[])

        raise NotFoundException

    @staticmethod
    async def delete_by_endpoint(endpoints: list[str], db_client):
        for endpoint in endpoints:
            await db_client.delete_data(endpoint)

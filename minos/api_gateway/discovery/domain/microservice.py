from __future__ import (
    annotations,
)

from ..exceptions import (
    NotFoundException,
)
from .endpoint import (
    ConcreteEndpoint,
    GenericEndpoint,
)

MICROSERVICE_KEY_PREFIX = "microservice"
ENDPOINT_KEY_PREFIX = "endpoint"


class Microservice:
    """Microservice class."""

    def __init__(self, name: str, address: str, port: int, endpoints: list[list[str]], status: bool = True):
        self.name = name
        self.address = address
        self.port = port
        self.endpoints: list[GenericEndpoint] = [
            GenericEndpoint(endpoint_verb, endpoint_path) for endpoint_verb, endpoint_path in endpoints
        ]
        self.status = status

    @classmethod
    async def find_by_endpoint(cls, concrete_endpoint: ConcreteEndpoint, db_client) -> Microservice:
        """Find a microservice bt endpoint.

        :param concrete_endpoint: The concrete endpoint that must match.
        :param db_client: The database client.
        :return: A ``Microservice`` instance.
        """
        async for key_bytes in db_client.redis.scan_iter(match=f"{ENDPOINT_KEY_PREFIX}:{concrete_endpoint.verb}:*"):
            endpoint = GenericEndpoint.load_by_key(key_bytes)
            if endpoint.matches(concrete_endpoint):
                return await cls.load_by_endpoint(key_bytes, db_client)

        raise NotFoundException

    @classmethod
    async def load_by_endpoint(cls, endpoint_key: bytes, db_client) -> Microservice:
        """Load an instance from the database.

        :param endpoint_key: The endpoint key.
        :param db_client: The database client.
        :return: A ``Microservice`` instance.
        """
        microservice_key = await db_client.get_data(endpoint_key)
        return await cls.load(microservice_key, db_client)

    @classmethod
    async def load(cls, microservice_key: bytes, db_client) -> Microservice:
        """Load an instance from the database.

        :param microservice_key: The microservice key.
        :param db_client: The database client.
        :return: A ``Microservice`` instance.
        """

        microservice_dict = await db_client.get_data(microservice_key)
        microservice_dict["endpoints"] = [
            endpoint_key.split(":", 2)[1:] for endpoint_key in microservice_dict["endpoints"]
        ]
        return cls(**microservice_dict)

    async def save(self, db_client) -> None:
        """Store the instance into the database.

        :param db_client: The database client.
        :return: This method does not return anything.
        """
        microservice_value = {
            "name": self.name,
            "address": self.address,
            "port": self.port,
            "endpoints": [
                f"{ENDPOINT_KEY_PREFIX}:{endpoint.verb}:{endpoint.path_as_str}" for endpoint in self.endpoints
            ],
            "status": self.status,
        }

        microservice_key = f"{MICROSERVICE_KEY_PREFIX}:{self.name}"
        await db_client.set_data(microservice_key, microservice_value)
        for endpoint_key in microservice_value["endpoints"]:
            await db_client.set_data(endpoint_key, microservice_key)

    @classmethod
    async def delete(cls, microservice_name, redis_client):
        microservice_label = f"{MICROSERVICE_KEY_PREFIX}:{microservice_name}"
        microservice_data = await redis_client.get_data(microservice_label)
        endpoints = microservice_data["endpoints"]
        await redis_client.delete_data(microservice_label)
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

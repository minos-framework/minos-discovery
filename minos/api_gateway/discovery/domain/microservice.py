from typing import NoReturn

from .endpoint import Endpoint
from ..exceptions import NotFoundException


class Microservice:
    def __init__(self, name: str, address: str, port: int, endpoints: list[str]):
        self.name = name
        self.address = address
        self.port = port
        self.endpoints = [Endpoint(endpoint_name) for endpoint_name in endpoints]

    def save(self, db_client) -> NoReturn:
        microservice_value = {
            "name": self.name,
            "address": self.address,
            "port": self.port
        }

        for endpoint in self.endpoints:
            db_client.set_data(endpoint.name, microservice_value)

    @classmethod
    def find_by_endpoint(cls, name, db_client) -> "Microservice":
        microservice_dict = db_client.get_data(name)
        if not microservice_dict:
            raise NotFoundException

        microservice = cls(**microservice_dict, endpoints=[])

        return microservice

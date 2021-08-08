from .endpoint import Endpoint


class Microservice:
    def __init__(self, name: str, address: str, port: int, endpoints: list[str]):
        self.name = name
        self.address = address
        self.port = port
        self.endpoints = [Endpoint(endpoint_name) for endpoint_name in endpoints]

    def save(self, db_client):
        microservice_value = {
            "name": self.name,
            "address": self.address,
            "port": self.port
        }

        for endpoint in self.endpoints:
            db_client.set_data(endpoint.name, microservice_value)

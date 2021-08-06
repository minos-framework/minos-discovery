class Microservice:
    def __init__(self, name: str, address: str, port: int, endpoints: list[str]):
        self.name = name
        self.address = address
        self.port = port
        self.endpoints = endpoints

from abc import (
    ABC,
)

from .exceptions import (
    CannotInstantiateException,
)


class PathPart:
    def __init__(self, name: str):
        self.name = name
        self.is_generic: bool = True if self.name.startswith("{") and self.name.endswith("}") else False


class Endpoint:
    def __init__(self, verb: str, path: str):
        self.verb = verb
        self.path: tuple[PathPart] = tuple(PathPart(path_part) for path_part in path.split("/"))

    @property
    def path_as_str(self) -> str:
        return "/".join([str(part.name) for part in self.path])


class ConcreteEndpoint(Endpoint):
    def __init__(self, verb: str, path: str):
        super().__init__(verb, path)
        for part in self.path:
            if part.is_generic:
                raise CannotInstantiateException


class GenericEndpoint(Endpoint):
    def matches(self, concrete_endpoint: ConcreteEndpoint) -> bool:
        if self.verb != concrete_endpoint.verb:
            return False

        if len(self.path) != len(concrete_endpoint.path):
            return False
        for path_part, concrete_path_part in zip(self.path, concrete_endpoint.path):
            if path_part.name != concrete_path_part.name and not path_part.is_generic:
                return False

        return True

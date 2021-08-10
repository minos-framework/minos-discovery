class Endpoint:
    def __init__(self, path: str):
        self.path = path

    def matches(self, url: str) -> bool:
        path_parts = self.path.split("/")
        url_parts = url.split("/")
        if len(path_parts) != len(url_parts):
            return False

        for path_part, url_part in zip(path_parts, url_parts):
            if path_part != url_part and not path_part.startswith("{") and not path_part.endswith("}"):
                return False

        return True

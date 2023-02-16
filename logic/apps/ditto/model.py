from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Request:
    method: str = None
    url: str = None
    headers: dict[str, object] = field(default_factory={})


@dataclass
class Response:
    status: int = None
    body: str = None


@dataclass
class Ditto:
    name: str
    request: Request = None
    response: Response = None

    def __init__(self, request: Request, response: Response, name: str = None) -> 'Ditto':

        self.name = name
        self.request = request
        self.response = response

        if not name:
            self.name = str(uuid4()).split('-')[0]

    def __eq__(self, other):
        return self.name == other.name

from dataclasses import dataclass, field

from logic.apps.ditto.model import Ditto


@dataclass
class Team:
    name: str = None
    dittos: list[Ditto] = field(default_factory=[])

    def __eq__(self, other):
        return self.name == other.name

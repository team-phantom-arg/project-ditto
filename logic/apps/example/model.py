from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.sql.sqltypes import Integer


@dataclass
class Example(object):
    id: Integer = None
    string: str = None
    integer: int = None
    date_time: datetime = None
    double: float = None
    uuid: UUID = field(default_factory=uuid4)

    def __eq__(self, other):
        return self.id == other.id

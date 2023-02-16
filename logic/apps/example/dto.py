from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from uuid import UUID, uuid4

from logic.apps.example.model import Example


def example_to_json(o: Example) -> Dict[str, object]:

    return {
        'id': o.id,
        'string': o.string,
        'integer': o.integer,
        'date_time': o.date_time.isoformat(),
        'double': o.double,
        'uuid': str(o.uuid)
    }


def json_to_example(o: Dict[str, object]) -> Example:

    return Example(
        string=o.get('string'),
        integer=int(o.get('integer')),
        date_time=datetime.fromisoformat(o.get('date_time')),
        double=float(o.get('double')),
        uuid=UUID(o.get('uuid')) if 'uuid' in o else uuid4()
    )

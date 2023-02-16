from typing import Dict

from logic.apps.ditto.model import Ditto


def yaml_to_ditto(o: Dict[str, object]) -> Ditto:
    return Ditto()


def ditto_to_dict(d: Ditto) -> dict[str, object]:

    request = {
        'url': d.request.url,
        'method': d.request.method,
        'headers': d.request.headers
    }

    response = {
        'status': d.response.status,
        'body': d.response.body
    }

    return {
        'name': d.name,
        'request': request,
        'response': response,
    }

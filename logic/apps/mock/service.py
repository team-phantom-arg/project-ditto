import json

from flask import Request, Response, jsonify

from logic.apps.ditto.model import Ditto
from logic.apps.team import service as team_service


def _ditto_match_request(ditto: Ditto, request: Request) -> bool:

    if request.path != ditto.request.url:
        return False

    if request.method != ditto.request.method:
        return False

    if ditto.request.headers:

        for k in ditto.request.headers.keys():

            if request.headers.get(k) != ditto.request.headers.get(k):
                return False

    return True


def get_ditto_match_request(request: Request) -> bool:

    for t in team_service.get_all():
        for d in t.dittos:
            if _ditto_match_request(d, request):
                return d

    return None


def _is_json(body: str) -> bool:
    try:
        json.loads(body)
        return True

    except Exception:
        return False


def eval_ditto(ditto: Ditto):

    body = ditto.response.body
    body_final = json.loads(body) if _is_json(body) else body

    headers = ditto.response.headers

    if _is_json(body_final):
        headers['Content-Type'] = 'application/json'

    return body_final, ditto.response.status, headers

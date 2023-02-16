from flask import Blueprint, request
from flask.json import jsonify
from logic.apps.example.error import ExampleError
from logic.apps.example import dto
from logic.apps.example import service
from logic.libs.exception.exception import AppException

import yaml
from logic.apps.team import dto, service
from logic.apps.team.model import Team

blue_print = Blueprint('team', __name__, url_prefix='/api/v1/teams')


@blue_print.route('/', methods=['GET'])
def get():

    result = []
    teams = service.get_all()
    for t in teams:
        result.append(dto.team_to_dict(t))

    return result, 200


@blue_print.route('/', methods=['POST'])
def post():

    dict_yaml = yaml.load(request.body, Loader=yaml.Loader)

    m = dto.dict_to_team(dict_yaml)
    service.add(m)

    return "", 201

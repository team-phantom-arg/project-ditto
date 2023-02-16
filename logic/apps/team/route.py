import yaml
from flask import Blueprint, request

from logic.apps.team import dto, service

blue_print = Blueprint('team', __name__, url_prefix='/api/v1/teams')


@blue_print.route('/', methods=['GET'])
def get():

    result = []
    teams = service.get_all()
    for t in teams:
        result.append(dto.team_to_dict(t))

    return result[0], 200


@blue_print.route('/', methods=['POST'])
def post():

    dict_yaml = yaml.load(request.data, Loader=yaml.Loader)

    m = dto.dict_to_team(dict_yaml)
    service.add(m)

    return "", 201

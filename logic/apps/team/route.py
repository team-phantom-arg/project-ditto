import yaml
from flask import Blueprint, request, jsonify

from logic.apps.team import dto, service

blue_print = Blueprint('team', __name__, url_prefix='/api/v1/teams')


@blue_print.route('/', methods=['GET'])
def list_all():

    return jsonify(service.list_all()), 200


@blue_print.route('/', methods=['POST'])
def post():

    dict_yaml = yaml.load(request.data, Loader=yaml.Loader)

    m = dto.dict_to_team(dict_yaml)
    service.add(m)

    return "", 201


@blue_print.route('/<name>', methods=['GET'])
def get(name: str):

    team = service.get(name)
    return jsonify(dto.team_to_dict(team)), 200


@blue_print.route('/<name>', methods=['DELETE'])
def delete(name: str):

    service.delete(name)

    return "", 200

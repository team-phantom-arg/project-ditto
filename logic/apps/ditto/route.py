from flask import Blueprint, jsonify

from logic.apps.ditto import dto, service

blue_print = Blueprint(
    'dittos', __name__, url_prefix='/api/v1/teams/<team>/dittos')


@blue_print.route('/', methods=['GET'])
def list_all(team: str):
    return jsonify(service.list_all(team)), 200


@blue_print.route('/<ditto>', methods=['GET'])
def get(team: str, ditto: str):

    ditto = service.get(team, ditto)
    return dto.ditto_to_dict(ditto), 200


@blue_print.route('/all', methods=['GET'])
def get_all(team: str):
    dittos = service.get_all(team)
    return jsonify([dto.ditto_to_dict(d) for d in dittos]), 200

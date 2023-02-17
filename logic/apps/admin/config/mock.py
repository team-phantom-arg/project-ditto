import yaml
from flask import request

from logic.apps.mock import service
from logic.apps.team import service as team_service
from logic.apps.team.dto import dict_to_team
import os

_PATH_YAML_FILE = 'config.yaml'


def setup_mocks(app):
    @app.before_request
    def mock():
        print(request.method)
        print(request.path)
        print(request.headers)

        ditto = service.get_ditto_match_request(request)
        if ditto:
            return service.eval_ditto(ditto)


def setup_start_file():

    if not os.path.exists(_PATH_YAML_FILE):
        return

    with open(_PATH_YAML_FILE, 'r') as file:
        yaml_dict = yaml.load(file.read(), Loader=yaml.Loader)

    for d in yaml_dict:
        team = dict_to_team(d)
        team_service.add(team)

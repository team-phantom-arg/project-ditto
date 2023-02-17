from logic.apps.ditto.model import Ditto
from logic.apps.team import service as team_service
from logic.apps.team.error import TeamError
from logic.libs.exception.exception import AppException


def get_all(team_name: str) -> list[Ditto]:

    team = team_service.get(team_name)
    if not team:
        msj = f'Team with name {team_name} not exist'
        raise AppException(TeamError.TEAM_NOT_EXIST_ERROR, msj)

    return team.dittos


def get(team_name: str, ditto_name: str) -> Ditto:

    for d in get_all(team_name):
        if d.name == ditto_name:
            return d

    return None


def list_all(team_name: str) -> list[Ditto]:

    return [d.name for d in get_all(team_name)]

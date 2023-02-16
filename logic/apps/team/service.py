from logic.apps.team.error import TeamError
from logic.apps.team.model import Team
from logic.libs.exception.exception import AppException

_TEAMS = []


def add(team: Team):

    global _TEAMS

    if team in _TEAMS:
        msj = f'Team with name {team.name} already exist'
        raise AppException(TeamError.TEAM_EXIST_ERROR, msj)

    _TEAMS.append(team)


def get_all() -> list[Team]:

    global _TEAMS
    return _TEAMS


def get(name: str) -> Team:

    global _TEAMS

    for t in _TEAMS:
        if t.name == name:
            return t

    return None

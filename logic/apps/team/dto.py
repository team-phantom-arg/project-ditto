from typing import Dict

from logic.apps.team.model import Team
from logic.apps.ditto.model import Ditto, Request, Response
from logic.apps.ditto.dto import ditto_to_dict


def dict_to_team(o: Dict[str, object]) -> Team:

    dittos = []
    for dict_ditto in o.get('dittos'):

        ditto = Ditto(
            request=Request(
                method=dict_ditto['request']['method'],
                url=dict_ditto['request']['url'],
                headers=dict_ditto['request'].get('headers', {})
            ),
            response=Response(
                status=dict_ditto['response'].get('status', 200),
                body=dict_ditto['response'].get('body', ''),
                headers=dict_ditto['response'].get('headers', {})
            )
        )

        if dict_ditto.get('name', None):
            ditto.name = dict_ditto['name']

        dittos.append(ditto)

    return Team(
        name=o.get('name'),
        dittos=dittos
    )


def team_to_dict(t: Team) -> dict[str, object]:

    dittos = []
    for d in t.dittos:
        dittos.append(ditto_to_dict(d))

    return {
        'name': t.name,
        'dittos': dittos
    }

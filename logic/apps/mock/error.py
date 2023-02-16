from enum import Enum


class TeamError(Enum):
    YAML_ERROR = 'YAML_ERROR'
    TEAM_EXIST_ERROR = 'TEAM_EXIST_ERROR'
    TEAM_NOT_EXIST_ERROR = 'TEAM_NOT_EXIST_ERROR'

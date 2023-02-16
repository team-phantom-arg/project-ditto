from enum import Enum

from logic.libs.variables.variables import Config, get_var, setup


class Vars(Enum):
    VERSION = 'VERSION'
    PYTHON_HOST = 'PYTHON_HOST'
    PYTHON_PORT = 'PYTHON_PORT'
    LOGS_LEVEL = 'LOGS_LEVEL'
    LOGS_PATH = 'LOGS_PATH'
    LOGS_BACKUPS = 'LOGS_BACKUPS'
    DB_SQLITE_LOGS = 'DB_SQLITE_LOGS'
    DB_SQLITE_PATH = 'DB_SQLITE_PATH'


def setup_vars():
    setup(
        Config(
            file_path='logic/resources/variables.yaml',
            hiden_vars=['DB_SQLITE_PATH']
        )
    )

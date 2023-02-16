from pathlib import Path

from logic.libs.sqliteAlchemy.sqliteAlchemy import Config, setup
from logic.libs.variables.variables import get_var

from .variables import Vars


def setup_sqlite():

    setup(
        Config(
            url=get_var(Vars.DB_SQLITE_PATH),
            echo=False,
            path='logic/apps/*/entity.*'
        )
    )

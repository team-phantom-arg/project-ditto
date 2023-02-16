"""
SQLiteAlchemy
---------
1.0.0

Utiliza sqlAlchemy para establecer una uncia conexion con un sqlite local, es para uso simple sin tanta configuracion.
Requiere de la libreria de Reflection
"""
from dataclasses import dataclass
from typing import Any

from logic.libs.reflection import reflection
from logic.libs.sqliteAlchemy.src import config
from logic.libs.sqliteAlchemy.src.sqlAlchemyMethods import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


@dataclass
class Config():
    """
    Objeto de configuracion
    """
    url: str = ':memory:'
    echo: bool = False
    path: str = ''


def setup(conf: Config):
    """
    Configura la util, se debe usar antes de usar cualquier otro metodo
    """
    config.URL = conf.url
    config.ECHO = conf.echo
    config.ENGINE = create_engine(conf.url)

    for module_type in reflection.load_modules_by_regex_path(conf.path):
        module_type.Entity.metadata.create_all(config.ENGINE)


def make_session() -> Session:
    """
    Crea una nueva session para conectarse a la BD
    """
    if not config.ENGINE:
        create_engine()

    return sessionmaker(config.ENGINE)()


def get_entity_class() -> Any:
    """
    Crea la clase Entity del que deben heredar todos los entities
    """
    return declarative_base()

"""
Variables
---------
1.0.0

Utiliza un archivo .env para crear un diccionario usado como variables del proyecto, 
en caso de que exista la variable de ambiente en el sistema utiliza esa, 
en caso de que no, usa la del archivo 
"""
import os
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from logic.libs.variables.src.file import make_vars_dict

DICT_VARS: Dict[str, str] = {}
HIDEN_VARS: List[str] = []


@dataclass
class Config:
    """
    Objeto de configuracion
    """
    file_path: str
    hiden_vars: List[str]


def setup(cfg: Config):
    """
    Configura la util, se debe usar antes de usar cualquier otro metodo

    - configs -> lista de objetos de configuracion
    """
    global DICT_VARS, HIDEN_VARS

    DICT_VARS.update(make_vars_dict(cfg.file_path))
    HIDEN_VARS.extend(cfg.hiden_vars)


def get_var(var: Enum) -> str:
    """
    Obtiene el valor de la variable de entorno correspondiente, en caso de no obtenerla,
    la saca del diccionario de variables predefinidas
    """
    if isinstance(var, Enum):
        var = var.value

    global DICT_VARS
    default_value = DICT_VARS.get(var)

    return os.environ.get(var, default_value)


def all_vars() -> Dict[str, str]:
    """
    Devuelve el mapa de variables con sus valores instanciados y filtrados por la lista de no mostrados
    """
    global DICT_VARS, HIDEN_VARS
    return {
        key: get_var(key)
        for key in DICT_VARS
        if key not in HIDEN_VARS
    }

import os
import re
from typing import Any

_REGEX_EXTRAER_VARIABLE = r'\$\{[^\}]+\:*[^\}]*\}'
_REGEX_TIENE_VARIABLE = r'[^\$]*' + _REGEX_EXTRAER_VARIABLE + r'[^\$]*'


def _is_a_env_var(variable: str) -> bool:
    """
    Debuelve verdadero si la variable tiene el formato 
    de una variable de ambiente
    """
    return re.match(_REGEX_TIENE_VARIABLE, str(variable)) is not None


def _parse_env_var(key: str) -> str:
    """
    Obtiene el valor de la variable de entorno con el formato de ${VAR:default}
    """
    if not _is_a_env_var(key):
        return key

    for variable_ambiente in re.findall(_REGEX_EXTRAER_VARIABLE, key):
        var_y_default = variable_ambiente.replace(
            '${', '').replace('}', '').split(':', 1)

        var_ambiente = var_y_default[0]
        val_default = var_y_default[1] if len(var_y_default) > 1 else ''

        valor_final = os.environ.get(var_ambiente, val_default)

        key = key.replace(variable_ambiente, valor_final)

    return key


def parse_env_vars(obj: Any) -> Any:
    """
    Devuelve el diccionario con las variables de ambiente
    reemplazadas por su correspondiente valor
    """
    if isinstance(obj, dict):
        nuevo_d = {}
        for key, value in obj.items():
            nuevo_d[key] = parse_env_vars(value)
        return nuevo_d

    if isinstance(obj, list):
        return [
            parse_env_vars(elem)
            for elem in obj
        ]

    return _parse_env_var(obj)

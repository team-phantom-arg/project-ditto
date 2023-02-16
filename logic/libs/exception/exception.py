"""
Exception
---------
1.0.0

Objetos genericos para manejo de exepciones en los proyectos
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict


@dataclass
class AppException(Exception):
    """
    Clase de error basico para manejar errores de negocio o errores dentro de la aplicacion
    que son esperados sus atributos son:

    codigo: usado para quien quiera atrapar la excepcion, se puede usar un str de la forma 'ERROR_ALTA_USUARIO'
    o un codigo numerico, la idea es que alguien pueda hacer un if con este codigo pudiendo hacer algo al respecto

    mensaje: contiene informacion extra en formato texto para una mayor informacion, esto es para quien use la api,
    un ejemplo puede ser: 'el usuario ya existe en la base de datos'
    """
    code: Enum
    msj: str = None
    exception: Exception = None

    def to_json(self) -> Dict[str, object]:
        d = {'code': self.code.value, 'msj': self.msj}
        if self.exception:
            d['exception'] = str(self.exception)
        return d


@dataclass
class UnknownException(Exception):
    """
    Error desconocido, es basicamente para encapsular nuevos metodos para Exection
    """
    error: Exception

    def to_json(self) -> Dict[str, object]:
        d = {'cause': str(self.error)}
        return d

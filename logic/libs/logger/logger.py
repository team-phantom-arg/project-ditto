"""
Logger
-------
1.0.0

Crea logs de la aplicacion
"""
import logging
from dataclasses import dataclass
from typing import Dict, List

from logic.libs.logger.src.file import make_logger


logger: logging.Logger


@dataclass
class Config():
    """
    Objeto de configuracion
    """
    path: str = '/tmp/logs'
    level: str = 'INFO'
    file_backup_count: int = 3


def setup(config: Config):
    """
    Configura las opciones PREDEFINIDAS del logger para el proyecto, en caso del handler, 
    el que viene rota los logs con un archivo por dia hasta hasta un maximo de 7 archivos.
    """
    global logger
    logger = make_logger(config)

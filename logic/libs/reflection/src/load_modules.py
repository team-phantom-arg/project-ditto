"""
Herramienta que carga de formma dinamica los blueprints de flask recursivamente
que se encuentren en un directorio
"""
import glob
import os
from typing import List


def file_name(path: str) -> str:
    """
    Devuelve el nombre del archivo al final de la ruta sin la extension
    """
    return os.path.basename(path).split('.')[0]


def get_modules_paths(base_path: str) -> List[str]:
    """
    Obtiene las rutas de todos los archivos .py dentro del directorio parametro, 
    es recursivo por lo que si hay carpetas dentro tambien busca ahi
    """
    if os.path.isfile(base_path):
        return [base_path]

    blueprints_routes = []

    for root, _, files in os.walk(base_path):

        if '__pycache__' in root or not files:
            continue

        blueprints_routes.extend([
            os.path.join(root, file)
            for file in files
        ])

    return blueprints_routes


def get_modules_paths_by_regex(regex_path: str) -> List[str]:
    """
    Obtiene las rutas de todos los archivos python dentro del directorio parametro regex, 
    es recursivo por lo que si hay carpetas dentro tambien busca ahi
    """
    paths = []

    for base_path in glob.glob(regex_path):
        paths.extend(get_modules_paths(base_path))

    return paths

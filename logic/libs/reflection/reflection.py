"""
Reflection
---------
1.0.0

Herramientas de reflection muy variadas
"""
from importlib.util import module_from_spec, spec_from_file_location
from types import ModuleType
from typing import List

from logic.libs.reflection.src import load_modules


def get_module_by_path(module_path: str) -> ModuleType:
    """
    Carga el modulo del archivo python del a ruta parametro, no ejecuta nada, solo hace un import y devuelve el modulo importado
    """
    module_name = load_modules.file_name(module_path)

    spec = spec_from_file_location(module_name, module_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def load_modules_by_path(modules_path: str) -> List[ModuleType]:
    """
    Carga los archivos python recursivamente dentro del directorio, no ejecuta ningun metodo, simplemente hace un import de los mismos.\n
    Es posible pasarle una regex. \n
    Ejemplo:
    ```
    'logic/apps/routes'
    ```
    """
    modules = []
    for path in load_modules.get_modules_paths(modules_path):
        modules.append(get_module_by_path(path))

    return modules


def load_modules_by_regex_path(modules_path: str) -> List[ModuleType]:
    """
    Igual que load_modules_by_path() pero se le puede pasar un regex.\n
    Ejemplo:
    ```
    'logic/apps/*/routes'
    ```
    """
    modules = []
    for path in load_modules.get_modules_paths_by_regex(modules_path):
        modules.append(get_module_by_path(path))
    return modules

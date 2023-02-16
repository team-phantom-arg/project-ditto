from typing import Dict

import yaml


def make_vars_dict(file_path: str) -> Dict[str, str]:
    """
    Genera un diccionario con las variables del archivo enviado por 
    parametro parseadas con sus respectivas variables de ambiente
    """
    with open(file_path, 'r') as file:
        dic_yaml = yaml.load(file, Loader=yaml.FullLoader)

    return dic_yaml

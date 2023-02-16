import logging
import os
from logging.handlers import TimedRotatingFileHandler


def make_logger(config) -> logging.Logger:
    """
    Devuelve un objeto logger por un nombre, en caso de que no exista lo crea
    """
    dir_path = os.path.dirname(config.path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s (%(process)d) - %(levelname)s - %(message)s')

    fh = TimedRotatingFileHandler(
        config.path,
        when="d",
        interval=1,
        backupCount=config.file_backup_count)
    fh.setLevel(config.level)
    fh.setFormatter(formatter)

    sh = logging.StreamHandler()
    sh.setLevel(config.level)
    sh.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(config.level)
    logger.addHandler(fh)
    logger.addHandler(sh)

    return logger

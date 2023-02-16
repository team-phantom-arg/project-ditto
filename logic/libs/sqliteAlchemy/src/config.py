from sqlalchemy.engine import Engine

URL_DEFAULT: str = ':memory:'
URL: str = URL_DEFAULT
ECHO: bool = False

ENGINE: Engine = None

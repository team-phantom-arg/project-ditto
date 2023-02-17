from flask import Flask
from werkzeug.exceptions import HTTPException

from logic.libs.exception.exception import AppException, UnknownException
from logic.libs.logger import logger


def add_decorators(app: Flask):
    """
    Carga el handler de error basico para manejo de AppExceptions y excepciones comunes
    """
    @app.errorhandler(HTTPException)
    def handle_exception(httpe):
        return '', httpe.code

    @app.errorhandler(AppException)
    def handle_business_exception(ae: AppException):
        logger.logger.warning(ae.to_json())
        return ae.to_json(), 409

    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        logger.logger.exception(e)
        return UnknownException(e).to_json(), 500

    @app.after_request
    def apply_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        return response

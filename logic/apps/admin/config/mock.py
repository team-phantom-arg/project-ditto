from flask import request

from logic.apps.mock import service


def setup_mocks(app):
    @app.before_request
    def mock():
        print(request.method)
        print(request.path)
        print(request.headers)

        ditto = service.get_ditto_match_request(request)
        if ditto:
            print('encontre ditto')
            return service.eval_ditto(ditto)

from flask import Flask
from logic.libs.rest.rest import setup


def setup_rest(app: Flask) -> Flask:

    setup(app, [
        'logic/apps/admin/routes/admin_route.*',
        'logic/apps/*/route.*'
    ])

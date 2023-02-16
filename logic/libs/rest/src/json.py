from datetime import date

from flask.json import JSONEncoder


class JSONEncoderCustom(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def config_encoders(flask_app):
    """
    Configura los json encoders
    """
    flask_app.json_encoder = JSONEncoderCustom

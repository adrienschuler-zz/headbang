import falcon

from app import _models


class Places():
    def __init__(self):
        pass

    def on_get(self, req, resp) -> dict:
        resp.media = _models['place'].show()
        resp.status = falcon.HTTP_200

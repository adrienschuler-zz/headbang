import json

import falcon

from app import _models


class Places():
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.media = _models['place'].show()
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if req.content_length:
            places = json.load(req.stream)
            resp.media = _models['place'].post(places)

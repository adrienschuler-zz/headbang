import json

import falcon

from app import Log, Models


class Places:
    def __init__(self):
        pass

    def on_get(self, req, resp):
        places = Models.Place.show()
        Log.debug(places)
        resp.media = places
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if req.content_length:
            places = json.load(req.stream)
            resp.media = Models.Place.post(places)

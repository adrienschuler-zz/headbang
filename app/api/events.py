import json
import falcon

from app import Log, Models


class Events:
    def __init__(self):
        pass

    def on_get(self, req, resp):
        events = Models.Event.get()
        Log.debug(events)
        resp.media = events
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if req.content_length:
            events = json.load(req.stream)
            resp.media = Models.Event.post(events)

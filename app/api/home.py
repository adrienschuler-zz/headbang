import json
import falcon

from app import Config, Models
from app.utils import load_template


class Home:
    def __init__(self):
        pass

    def on_get(self, req, resp):
        places = Models.Place.get(size=5)
        fbids = Models.Place.get_facebook_ids(size=100)

        template = load_template('index')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render(
            google_api_key=Config.apis['google']['api_key'],
            places=places,
            fbids=fbids)

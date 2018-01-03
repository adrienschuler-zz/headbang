import falcon

from app import _config
from app.utils import load_template


class Views():

    def __init__(self):
        pass

    def on_get(self, req, resp):
        template = load_template('index')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render(google_api_key=_config['apis']['google']['api_key'])

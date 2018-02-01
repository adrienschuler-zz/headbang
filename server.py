import os
import falcon

from app import Log

from app.api.home import Home
from app.api.places import Places
from app.api.events import Events


api = falcon.API()

api.add_route('/', Home())
api.add_route('/places', Places())
api.add_route('/events', Events())
api.add_static_route('/assets', '%s/app/assets' % os.getcwd())

Log.info('🤘  HEADBANG 🤘')

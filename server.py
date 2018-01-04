import falcon

from app import Log, Config, Storage, Models

from app.api.home import Home
from app.api.places import Places

from app.models.place import Place

from app.storage.elasticsearch import ES


Storage.Elasticsearch = ES(Config.storage['elasticsearch'])

Models.Place = Place()

api = falcon.API()

api.add_route('/', Home())
api.add_route('/places', Places())

Log.info('🤘  HEADBANG 🤘')

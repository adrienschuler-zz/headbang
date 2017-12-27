import falcon

from app import _config, _models, _storage

from app.utils import load_conf
from app.storage.elasticsearch import ES

from app.models.place import Place
from app.api.places import Places


_config['apis'] = load_conf('apis')
_config['storage'] = load_conf('storage')

_storage['es'] = ES(_config['storage']['elasticsearch'])

_models['place'] = Place()

app = falcon.API()

app.add_route('/places', Places())

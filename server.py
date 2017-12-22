from flask import Flask

from app import config, models, storage

from app.utils import load_conf
from app.core.storage.elasticsearch import ES

from app.core.models.place import Place
from app.core.api.places import Places


config['apis'] = load_conf('apis')
config['storage'] = load_conf('storage')

storage['es'] = ES(config['storage']['elasticsearch'])

print(storage)

models['place'] = Place

app = Flask(__name__)

app.register_blueprint(Places)

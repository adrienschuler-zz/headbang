from app.utils import load_conf, Logger

from app.models.place import Place
from app.models.event import Event

from app.storage.elasticsearch import ES


Log = Logger()


class Config:
    apis = load_conf('apis')
    storage = load_conf('storage')


class Storage:
    Elasticsearch = ES(Config.storage['elasticsearch'])


class Models:
    Place = Place(storage=Storage)
    Event = Event(storage=Storage)

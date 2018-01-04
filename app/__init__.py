import sys
import logging

from app.utils import load_conf


class Config:
    apis = load_conf('apis')
    storage = load_conf('storage')


class Models:
    pass


class Storage:
    pass


Log = logging.getLogger('headbang')
handler = logging.StreamHandler(sys.stdout)
Log.addHandler(handler)
Log.setLevel(logging.DEBUG)
Log.propagate = True

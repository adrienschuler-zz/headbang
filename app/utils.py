import os

from yaml import load


def load_conf(filename):
    '''Get configuration from yaml filename.'''

    path = os.path.dirname(__file__) + '/config/' + filename + '.yml'
    return load(open(path, 'r'))

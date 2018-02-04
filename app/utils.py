import os
import sys
import logging

from yaml import load


class Logger:
    def __init__(self):
        handler = logging.StreamHandler(sys.stdout)
        self.log = logging.getLogger('headbang')
        self.log.addHandler(handler)
        self.log.setLevel(logging.DEBUG)
        self.log.propagate = True

    def debug(self, msg):
        self.log.debug(msg)

    def info(self, msg):
        self.log.info(msg)

    def warn(self, msg):
        self.log.warn(msg)

    def error(self, msg):
        self.log.error(msg)


def load_conf(filename):
    '''
    Get configuration from yaml filename.
    '''
    path = os.path.dirname(__file__) + '/config/' + filename + '.yml'
    return load(open(path, 'r'))


def remove_duplicates(li):
    '''
    Remove duplicates from a list and keep order
    '''
    check = set()
    result = []
    for item in li:
        if item not in check:
            result.append(item)
            check.add(item)
    return result

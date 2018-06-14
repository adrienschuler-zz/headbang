import os

from yaml import load


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

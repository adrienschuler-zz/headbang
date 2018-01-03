import os

from yaml import load

import jinja2


def load_conf(filename):
    '''Get configuration from yaml filename.'''

    path = os.path.dirname(__file__) + '/config/' + filename + '.yml'
    return load(open(path, 'r'))


def load_template(name):
    path = os.path.join('app', 'templates', '%s.j2' % name)
    with open(os.path.abspath(path), 'r') as fp:
        return jinja2.Template(fp.read())

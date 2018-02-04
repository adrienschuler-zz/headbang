import elasticsearch
from flask import Blueprint, jsonify


exceptions = Blueprint('exceptions', __name__)


@exceptions.app_errorhandler(elasticsearch.exceptions.ElasticsearchException)
@exceptions.app_errorhandler(elasticsearch.exceptions.ConnectionError)
@exceptions.app_errorhandler(elasticsearch.exceptions.TransportError)
@exceptions.app_errorhandler(elasticsearch.exceptions.NotFoundError)
@exceptions.app_errorhandler(elasticsearch.exceptions.RequestError)
def handle_notfound_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code


@exceptions.app_errorhandler(Exception)
def handle_unexpected_error(error):
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }

    return jsonify(response), status_code

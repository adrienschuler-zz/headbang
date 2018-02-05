import elasticsearch
from flask import Blueprint, jsonify


e = Blueprint('exceptions', __name__)


@e.app_errorhandler(elasticsearch.exceptions.ElasticsearchException)
@e.app_errorhandler(elasticsearch.exceptions.ConnectionError)
@e.app_errorhandler(elasticsearch.exceptions.TransportError)
@e.app_errorhandler(elasticsearch.exceptions.NotFoundError)
@e.app_errorhandler(elasticsearch.exceptions.RequestError)
def handle_notfound_error(error):
    message = [str(x) for x in error.args]
    response = {
        'success': False,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), error.status_code


@e.app_errorhandler(Exception)
def handle_unexpected_error(error):
    response = {
        'success': False,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }

    return jsonify(response), 500


@e.app_errorhandler(404)
def handle_page_not_found(error):
    response = {
        'success': False,
        'error': {
            'type': 'NotFound',
            'message': 'Page not found.'
        }
    }

    return jsonify(response), 404

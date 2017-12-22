from flask import Blueprint, jsonify


places = Blueprint('places', __name__)


@places.route('/places')
def show():
    return jsonify({'foo': 'bar'})

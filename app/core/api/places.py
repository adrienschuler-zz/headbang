from flask import Blueprint, jsonify
# from facebook import GraphAPIError

from app import models


Places = Blueprint('places', __name__)


@Places.route('/places')
@Places.route('/places/show')
def show() -> dict:
    return jsonify(models['place'].show())

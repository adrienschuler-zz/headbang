from flask import Flask, jsonify, render_template, request

from app import logging, Models
from app.exceptions import e


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

app.register_blueprint(e)


@app.route('/')
def home():
    places = Models.Place.get()
    return render_template('index.html', places=places)

# Places

@app.route('/places/', methods=['GET'])
def get_places():
    size = request.args.get('size', default=100, type=int)
    fields = request.args.get('fields', default='', type=str)

    if fields:
        fields = fields.split(',')

    places = Models.Place.get(size=size, fields=fields)
    return jsonify(places)


@app.route('/places/', methods=['POST'])
def post_places():
    response = Models.Place.post(request.get_json(force=True))
    return jsonify(response)


@app.route('/foursquare/venues/', methods=['GET'])
def get_foursquare_venues():
    size = request.args.get('size', default=100, type=int)
    venues = Models.Place.get_source('foursquare', size=size)
    return jsonify(venues)


@app.route('/foursquare/venues/', methods=['POST'])
def post_foursquare_venues():
    response = Models.Place.post_source('foursquare', request.get_json(force=True))
    return jsonify(response)


@app.route('/facebook/places/', methods=['GET'])
def get_facebook_places():
    size = request.args.get('size', default=100, type=int)
    places = Models.Place.get_source('facebook', size=size)
    return jsonify(places)


@app.route('/facebook/places/', methods=['POST'])
def post_facebook_places():
    places = Models.Place.post_source('facebook', request.get_json(force=True))
    return jsonify(places)


@app.route('/google/places/', methods=['GET'])
def get_google_places():
    size = request.args.get('size', default=100, type=int)
    places = Models.Place.get_source('google', size=size)
    return jsonify(places)


@app.route('/google/places/', methods=['POST'])
def post_google_places():
    places = Models.Place.post_source('google', request.get_json(force=True))
    return jsonify(places)

# Events

@app.route('/events/', methods=['GET'])
def get_events():
    size = request.args.get('size', default = 100, type = int)
    events = Models.Event.get(size=size)
    return jsonify(events)


@app.route('/events/', methods=['POST'])
def post_events():
    response = Models.Event.post(request.get_json(force=True))
    return jsonify(response)


logging.info('🤘  HEADBANG 🤘')

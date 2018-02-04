import jinja2
from flask import Flask, jsonify, render_template, request

from app import Log, Models
from app.exceptions import exceptions


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

app.register_blueprint(exceptions)


@app.route('/')
def home():
    size = request.args.get('size', default = 10, type = int)
    places = Models.Place.get(size=size)
    return render_template('index.html', places=places)


# Places

@app.route('/places/', methods=['GET'])
def get_places():
    size = request.args.get('size', default = 10, type = int)
    places = Models.Place.get(size=size)
    return jsonify(places)


@app.route('/places/', methods=['POST'])
def post_places():
    response = Models.Place.post(request.get_json(force=True))
    return jsonify(response)


@app.route('/places/fbids/', methods=['GET'])
def get_places_fbids():
    size = request.args.get('size', default = 10, type = int)
    places = Models.Place.get_fbids(size=size)
    return jsonify(places)


@app.route('/places/latlong/', methods=['GET'])
def get_places_latlong():
    size = request.args.get('size', default = 10, type = int)
    places = Models.Place.get_latlong(size=size)
    return jsonify(places)


# Events

@app.route('/events/', methods=['GET'])
def get_events():
    size = request.args.get('size', default = 10, type = int)
    events = Models.Event.get(size=size)
    return jsonify(events)


@app.route('/events/', methods=['POST'])
def post_events():
    response = Models.Event.post(request.get_json(force=True))
    return jsonify(response)


Log.info('🤘  HEADBANG 🤘')

from flask import Flask, jsonify, render_template, request

from app import Log, Models
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


Log.info('🤘  HEADBANG 🤘')

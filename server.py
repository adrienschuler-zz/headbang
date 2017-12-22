from flask import Flask

from core.models.places import places


app = Flask(__name__)

app.register_blueprint(places)

from flask import Flask

from models.places import places


app = Flask(__name__)

app.register_blueprint(places)

from dotenv import dotenv_values
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

config = dotenv_values(".env")

app = Flask("WashU Athletic Demographics API")
app.config["SQLALCHEMY_DATABASE_URI"] = config["POSTGRES_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.Athlete import *

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"


def serialize(objects, fields=None):
    serialized_list = []
    for o in objects:
        if fields:
            serialized_list.append(o.serialize())
        else:
            serialized_list.append(o.serialize())
    return serialized_list


@app.route("/api/athletes")
@cross_origin()
def get_athletes():
    data = Athlete.query.all()
    response = jsonify(serialize(data))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(debug=True)
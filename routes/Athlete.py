from models.Athlete import Athlete
from app import app
from flask import jsonify

def serialize(objects, fields=None):
    serialized_list = []
    for o in objects:
        if fields:
            serialized_list.append(o.serialize())
        else:
            serialized_list.append(o.serialize())
    return serialized_list

@app.route("/api/athletes", methods=["GET"])
def get_athletes():
    data = Athlete.query.all()
    return jsonify(serialize(data))

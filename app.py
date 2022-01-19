from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import dotenv_values

config = dotenv_values(".env")

print(config)

app = Flask("WashU Athletic Demographics API")
app.config["SQLALCHEMY_DATABASE_URI"] = config["POSTGRES_URI"]

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.Athlete import *
from routes.Athlete import *

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()

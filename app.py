from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask("WashU Athletic Demographics API")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://andrewhuang:password@localhost:5432/washu_athletes"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Athlete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.String(128))
    year = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    grade = db.Column(db.String(64))
    hometown = db.Column(db.String(128))
    highschool = db.Column(db.String(128))
    link = db.Column(db.String(256))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()

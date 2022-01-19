from app import db

class Athlete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.String(128))
    year = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    grade = db.Column(db.String(64))
    hometown = db.Column(db.String(128))
    hometown_latitude=db.Column(db.Float)
    hometown_longitude=db.Column(db.Float)
    highschool = db.Column(db.String(128))
    link = db.Column(db.String(256))

    def serialize(self):
        return {
            "id": self.id,
            "sport": self.sport,
            "year": self.year,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "grade": self.grade,
            "hometown": self.hometown,
            "hometown_latitude": self.hometown_latitude,
            "hometown_longitude": self.hometown_longitude,
            "highschool" : self.highschool,
            "link": self.link
        }
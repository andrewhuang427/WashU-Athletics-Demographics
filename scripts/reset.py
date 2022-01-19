from app import db
from models.Athlete import Athlete

Athlete.query.delete()
db.session.commit()

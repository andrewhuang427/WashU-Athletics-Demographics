import sys 
sys.path.append('../')
sys.path.append("./models")

from app import db
from models.Athlete import Athlete
  
Athlete.query.delete()
db.session.commit()

from . import db

from datetime import datetime

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True) 
    color = db.Column(db.String(255)) 
    size = db.Column(db.String(255)) 
    age = db.Column(db.Integer) 
    gender = db.Column(db.String(255)) 
    breed = db.Column(db.String(255)) 
    adopted = db.Column(db.Boolean, default=False) 
    date_added = db.Column(db.DateTime, default=datetime.utcnow) 
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color
        }
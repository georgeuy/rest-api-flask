from . import dog_bp
from .. import db
from ..models import Dog
from flask import jsonify, request


@dog_bp.get('/dogs')
def dogs():
    dogs = [dog.to_json() for dog in Dog.query.all()]
    response = jsonify({"data":dogs})
    return response, 200

@dog_bp.get('/dogs/create')
def create():

    dog = Dog()
    dog.name = 'Facha'
    dog.age = 10
    dog.adopted = True
    dog.gender = 'M'
    dog.color = 'Negro y Blanco'

    db.session.add(dog)
    db.session.commit()

    response = jsonify({"data": dog.to_json()})
    return response,201

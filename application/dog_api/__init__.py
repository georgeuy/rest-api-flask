from flask import Blueprint

dog_bp = Blueprint('dog', __name__)

from . import routes
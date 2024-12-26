import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ['CONFIGURATION_SETUP']

    app.config.from_object(environment_configuration)

    db.init_app(app) 

    with app.app_context():

        from .dog_api import dog_bp
        app.register_blueprint(dog_bp)

        return app

    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# importar as blueprints dos controlers

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    bcrypt.init_app(app)

    # app.register_blueprint('blueprint_importada')

    return app

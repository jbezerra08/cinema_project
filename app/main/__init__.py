from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

from .controller.usuario import usuario_blueprint
from .controller.filme import filme_blueprint
from .controller.sala import sala_blueprint
from .controller.sessao import sessao_blueprint


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(filme_blueprint)
    app.register_blueprint(sala_blueprint)
    app.register_blueprint(sessao_blueprint)

    return app

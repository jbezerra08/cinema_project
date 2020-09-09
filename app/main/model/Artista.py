from .. import db


class Artista(db.Model):
    """ Arstista Model para armazenar participantes de um filme """
    __tablename__ = 'artista'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)

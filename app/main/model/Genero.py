from .. import db


class Genero(db.Model):
    """ Genero Model para armazenar generos de filmes """
    __tablename__ = 'genero'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50), unique=True, nullable=False)

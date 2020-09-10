from .. import db


class Sala(db.Model):
    """ Sala Model para armazenar dados das salas """
    __tablename__ = 'sala'

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    total_assentos = db.Column(db.Integer, nullable=False)
    sessoes = db.relationship(
        'Sessao',
        backref='sala',
        lazy=True
    )

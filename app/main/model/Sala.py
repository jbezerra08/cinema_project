from .. import db


class Sala(db.Model):
    """ Sala Model para armazenar dados das salas """
    __tablename__ = 'sala'

    # implementar ORM

    def __init__(self, assentos):
        self.assentos = assentos

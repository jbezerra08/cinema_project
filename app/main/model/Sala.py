from .. import db


class Sala(db.Model):
    """ Sala Model para armazenar dados das salas """
    __tablename__ = 'sala'

    # implementar ORM

    assentos = db.Column(db.Integer, nullable=False)

    '''
    def __init__(self, assentos):
        self.assentos = assentos
    '''
from .. import db


class Sessao(db.Model):
    """ Sessao Model para armazenar dados das sessões """
    __tablename__ = 'sessao'

    # implementar ORM

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.DateTime, nullable=False)
    horario_inicio = db.Column(db.DateTime, nullable=False)

    '''
    def __init__(self, id, data, horario_inicio):
        self.id = id
        self.data = data
        self.horario_inicio = horario_inicio
    '''
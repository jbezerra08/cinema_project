from .. import db


class Sessao(db.Model):
    """ Sessao Model para armazenar dados das sessões """
    __tablename__ = 'sessao'

    # implementar ORM

    def __init__(self, id, data, horario_inicio):
        self.id = id
        self.data = data
        self.horario_inicio = horario_inicio

from .. import db


class Sessao(db.Model):
    """ Sessao Model para armazenar dados das sessões """
    __tablename__ = 'sessao'

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    total_tickets = db.Column(db.Integer, nullable=False)
    # entradas = db.relationship(
    #     'Entradas',
    #     backref='sessao',
    #     lazy=True
    # )
    # salas = db.relationship(
    #     'Sala',
    #     backref='sessao',
    #     lazy=True
    # )

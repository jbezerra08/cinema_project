from .. import db, ma
from .Ticket import Ticket, TicketSchema


class Sessao(db.Model):
    """ Sessao Model para armazenar dados das sessões """
    __tablename__ = 'sessao'

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    total_tickets = db.Column(db.Integer, nullable=False)
    filme_id = db.Column(
        db.Integer,
        db.ForeignKey('filme.id'),
        nullable=False
    )
    sala_id = db.Column(
        db.Integer,
        db.ForeignKey('sala.id'),
        nullable=False
    )
    tickets = db.relationship(
        'Ticket',
        backref='sessao',
        lazy=True
    )


class SessaoSchema(ma.Schema):
    tickets = ma.List(ma.Nested(TicketSchema))

    class Meta:
        model = Sessao
        fields = ('id', 'data', 'horario', 'total_tickets', 'tickets')


sessao_schema = SessaoSchema()
sessoes_schema = SessaoSchema(many=True)

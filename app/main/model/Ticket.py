from datetime import datetime

from .. import db, ma


class Ticket(db.Model):
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total_pago = db.Column(db.Float, nullable=False)
    validade = db.Column(db.Date, nullable=False)
    sessao_id = db.Column(
        db.Integer,
        db.ForeignKey('sessao.id'),
        nullable=True
    )
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id'),
        nullable=True
    )

    @staticmethod
    def verificar_validade(data_validade):
        return datetime.utcnow().date() <= datetime.strptime(data_validade, '%Y/%m/%d').date()


class TicketSchema(ma.Schema):
    class Meta:
        model = Ticket
        fields = (
            'id',
            'total_pago',
            'validade'
        )


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

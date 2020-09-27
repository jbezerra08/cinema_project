from .. import db, ma


class Ticket(db.Model):
    """ ticket Model para armazenar dados dos tickets """
    __tablename__ = 'ticket'

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total_pago = db.Column(db.Float, nullable=False)
    validade = db.Column(db.DateTime, nullable=False)
    sessao_id = db.Column(
        db.Integer,
        db.ForeignKey('sessao.id'),
        nullable=False
    )
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id'),
        nullable=False
    )

    @staticmethod
    def gerar_ticket():
        """ Criar ticket para um usuario """
        pass

    @staticmethod
    def verificar_validade():
        """ validade <= data atual """
        pass


class TicketSchema(ma.Schema):
    class Meta:
        model = Ticket
        fields = ('id', 'total_pago', 'validade')


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

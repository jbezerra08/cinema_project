from .. import db


class Ticket(db.Model):
    """ ticket Model para armazenar dados dos tickets """
    __tablename__ = 'ticket'

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, nullable=False)
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

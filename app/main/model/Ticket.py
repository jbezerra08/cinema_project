from .. import db


class Ticket(db.Model):
    """ Ticket Model para armazenar dados dos tickets """
    __tablename__ = 'ticket'

    # implementar ORM
    id_sessao = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    preco = db.Column(db.Float, nullable=False)
    validade = db.Column(db.DateTime, nullable=False)

    '''
    def __init__(self, sessao, usuario, preco, validade):
        self.sessao = sessao
        self.usuario = usuario
        self.preco = preco
        self.validade = validade
    '''
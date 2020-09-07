from .. import db


class Ticket(db.Model):
    """ Ticket Model para armazenar dados dos tickets """
    __tablename__ = 'ticket'

    # implementar ORM

    def __init__(self, sessao, usuario, preco, validade):
        self.sessao = sessao
        self.usuario = usuario
        self.preco = preco
        self.validade = validade

from .. import db


class Entrada(db.Model):
    """ Entrada Model para armazenar dados das entradas """
    __tablename__ = 'entrada'

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, nullable=False)
    validade = db.Column(db.DateTime, nullable=False)
    # sessao_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('sessao.id'),
    #     nullable=False
    # )
    # usuario_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey('usuario.id'),
    #     nullable=False
    # )

    @staticmethod
    def gerar_entrada():
        pass

    @staticmethod
    def verificar_validade():
        pass

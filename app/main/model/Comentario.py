from .. import db


class Comentario(db.Model):
    """ Comentario Model para armazenar os comentarios """
    __tablename__ = 'comentario'

    # implementar ORM

    id_filme = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    data = db.Column(db.Date, nullable=False)

    '''
    def __init__(self, filme, usuario, data, comentario):
        self.filme = filme
        self.usuario = usuario
        self.data = data
        self.comentario = comentario
    '''
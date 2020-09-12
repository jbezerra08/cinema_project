from .. import db


class Comentario(db.Model):
    """ Comentario Model para armazenar os comentarios """
    __tablename__ = 'comentario'

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.DateTime, nullable=False)
    texto_comentario = db.Column(db.Text, nullable=False)
    
    filme_id = db.Column(
        db.Integer,
        db.ForeignKey('filme.id'),
        nullable=False
    )
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id'),
        nullable=False
    )

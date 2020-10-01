from .. import db, ma


class Comentario(db.Model):
    __tablename__ = 'comentario'

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
        nullable=True
    )


class ComentarioSchema(ma.Schema):
    class Meta:
        model = Comentario
        fields = (
            'id',
            'data',
            'texto_comentario',
            'filme_id',
            'usuario_id'
        )


comentario_schema = ComentarioSchema()
comentarios_schema = ComentarioSchema(many=True)

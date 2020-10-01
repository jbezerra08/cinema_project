from .. import db, ma
from .Sessao import SessaoSchema


class Sala(db.Model):
    __tablename__ = 'sala'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer, nullable=False)
    total_assentos = db.Column(db.Integer, nullable=False)
    sessoes = db.relationship(
        'Sessao',
        cascade='all, delete',
        backref='sala',
        lazy=True
    )


class SalaSchema(ma.Schema):
    sessoes = ma.List(ma.Nested(SessaoSchema))

    class Meta:
        model = Sala
        fields = (
            'id',
            'numero',
            'total_assentos',
            'sessoes'
        )


sala_schema = SalaSchema()
salas_schema = SalaSchema(many=True)

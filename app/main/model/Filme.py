from .. import db, ma
from .Genero import GeneroSchema
from .Artista import ArtistaSchema
from .Sessao import SessaoSchema
from .Comentario import ComentarioSchema


generos = db.Table(
    'generos',
    db.Column(
        'genero_id', db.Integer, db.ForeignKey('genero.id'), primary_key=True
    ),
    db.Column(
        'filme_id', db.Integer, db.ForeignKey('filme.id'), primary_key=True
    )
)

participantes = db.Table(
    'participantes',
    db.Column(
        'artista_id', db.Integer, db.ForeignKey('artista.id'), primary_key=True
    ),
    db.Column(
        'filme_id', db.Integer, db.ForeignKey('filme.id'), primary_key=True
    )
)


class Filme(db.Model):
    """ Filme Model para armazenar dados dos filmes """
    __tablename__ = 'filme'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    lancamento = db.Column(db.Date, nullable=False)
    duracao = db.Column(db.String(50), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    sinopse = db.Column(db.Text, nullable=False)
    enredo = db.Column(db.Text, nullable=False)
    generos = db.relationship(
        'Genero',
        secondary=generos,
        backref=db.backref('generos', lazy=True)
    )
    elenco = db.relationship(
        'Artista',
        secondary=participantes,
        backref=db.backref('participantes', lazy=True)
    )
    sessoes = db.relationship(
        'Sessao',
        backref='filme',
        lazy=True
    )
    comentarios = db.relationship(
        'Comentario',
        backref='filme',
        lazy=True
    )


class FilmeSchema(ma.Schema):
    generos = ma.List(ma.Nested(GeneroSchema))
    elenco = ma.List(ma.Nested(ArtistaSchema))
    sessoes = ma.List(ma.Nested(SessaoSchema))
    comentarios = ma.List(ma.Nested(ComentarioSchema))

    class Meta:
        model = Filme
        fields = (
            'id',
            'titulo',
            'lancamento',
            'duracao',
            'registered_on',
            'sinopse',
            'enredo',
            'generos',
            'elenco',
            'sessoes',
            'comentarios'
        )


filme_schema = FilmeSchema()
filmes_schema = FilmeSchema(many=True)

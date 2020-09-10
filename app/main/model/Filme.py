from .. import db


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

    # implementar ORM
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    lancamento = db.Column(db.Date, nullable=False)  # ano, mes, dia
    duracao = db.Column(db.String(50), nullable=False)  # 120 minutos
    registered_on = db.Column(db.DateTime, nullable=False)
    sinopse = db.Column(db.Text, nullable=False)
    enredo = db.Column(db.Text, nullable=False)
    generos = db.relationship(
        'Genero',
        secondary=generos,
        backref=db.backref('generos', lazy='dynamic')
    )
    elenco = db.relationship(
        'Artista',
        secondary=participantes,
        backref=db.backref('participantes', lazy='dynamic')
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

    def __str__(self):
        return """
            'titulo': self.titulo,
            'lancamento': self.lancamento,
            'duracao': self.duracao,
            'registered_on': self.registered_on,
            'sinopse': self.sinopse,
            'enredo': self.enredo,
            'generos': [genero for genero in self.generos],
            'elenco': [artista for artista in self.elenco],
            'comentarios': [comentario for comentario in self.comentarios],
            'sessoes': [sessao for sessao in self.sessoes]
        """

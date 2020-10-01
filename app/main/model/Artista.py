from .. import db, ma


class Artista(db.Model):
    __tablename__ = 'artista'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)


class ArtistaSchema(ma.Schema):
    class Meta:
        model = Artista
        fields = (
            'id',
            'nome'
        )


artista_schema = ArtistaSchema()
artistas_schema = ArtistaSchema(many=True)

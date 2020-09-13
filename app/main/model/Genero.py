from .. import db, ma


class Genero(db.Model):
    """ Genero Model para armazenar generos de filmes """
    __tablename__ = 'genero'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50), unique=True, nullable=False)


class GeneroSchema(ma.Schema):
    class Meta:
        model = Genero
        fields = ('id', 'tipo')


genero_schema = GeneroSchema()
generos_schema = GeneroSchema(many=True)

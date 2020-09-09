from .. import db


class Filme(db.Model):
    """ Filme Model para armazenar dados dos filmes """
    __tablename__ = 'filme'

    # implementar ORM

    id = db.Column(db.Integer, orimary_key=True, autoincrement=True)
    #public_id = db.Column(db.String(100), unique=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    lancamento = db.Column(db.DateTime, nullable=False)
    duracao = db.column(db.DateTime, nullable=False)
    direcao = db.Column(db.String(250), nullable=False)
    producao = db.Column(db.String(250), nullable=False)
    sinopse = db.Column(db.Text, nullable=False)
    enredo = db.Column(db.String(250), nullable=False)
    avaliacao = db.Column(db.Integer, nullable=False)

    '''
    def __init__(self, id, titulo, genero, lancamento, duracao, direcao, producao, sinopse, enredo, avaliacao):

        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.lancamento = lancamento
        self.direcao = direcao
        self.producao = producao
        self.sinopse = sinopse
        self.enredo = enrendo
        self.avaliacao = avaliacao
    '''
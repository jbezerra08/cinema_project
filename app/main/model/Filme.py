from .. import db


class Filme(db.Model):
    """ Filme Model para armazenar dados dos filmes """
    __tablename__ = 'filme'

    # implementar ORM

    def __init__(self, id, titulo, genero, lancamento, duracao, direcao, producao, sinopse, enredo, avaliacao):

        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.lancamento = lancamento
        self.duracao = duracao
        self.direcao = direcao
        self.producao = producao
        self.sinopse = sinopse
        self.enredo = enrendo
        self.avaliacao = avaliacao

from datetime import datetime

from .. import db
from ..model.Filme import Filme, filme_schema, filmes_schema
from .Service_Genero import get_genero_by_tipo
from .Service_Artista import get_artista_by_nome


# adiciona apenas os generos e artistas previamente cadastrados
def add_filme(dados):
    filme = Filme.query.filter_by(titulo=dados['titulo']).first()
    if not filme:
        novo_filme = Filme(
            titulo=dados['titulo'],
            lancamento=datetime.strptime(dados['lancamento'], '%Y/%m/%d'),
            duracao=dados['duracao'],
            registered_on=datetime.utcnow(),
            sinopse=dados['sinopse'],
            enredo=dados['enredo']
        )
        [novo_filme.generos.append(obj) for obj in
            [get_genero_by_tipo(genero) for genero in dados['generos']]]
        [novo_filme.elenco.append(obj) for obj in
            [get_artista_by_nome(artista) for artista in dados['elenco']]]
        save(novo_filme)
        return novo_filme


def get_all_filmes():
    filmes = Filme.query.all()
    return filmes


def get_filme_by_id(id):
    filme = Filme.query.get(id)
    return filme


def get_filme_by_titulo(titulo):
    filme = Filme.query.filter_by(titulo=titulo).first()
    return filme


def update_filme(id, dados):
    filme = get_filme_by_id(id)
    if filme:
        filme.titulo = dados['titulo']
        filme.lancamento = dados['lancamento']
        filme.duracao = dados['duracao']
        filme.sinopse = dados['sinopse']
        filme.enredo = dados['enredo']
        db.session.commit()
        return filme


def delete_filme(id):
    filme = get_filme_by_id(id)
    if filme:
        delete(filme)
        return filme


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

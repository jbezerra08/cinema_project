from .. import db
from ..model.Artista import Artista


def add_artista(dados):
    artista = Artista.query.filter_by(nome=dados['nome']).first()
    if not artista:
        novo_artista = Artista(
            nome=dados['nome'],
        )
        save(novo_artista)
        return novo_artista


def get_all_artistas():
    artistas = Artista.query.all()
    return artistas


def get_artista_by_id(id):
    artista = Artista.query.get(id)
    return artista


def get_artista_by_nome(nome):
    artista = Artista.query.filter_by(nome=nome).first()
    return artista


def update_artista(id, dados):
    artista = get_artista_by_id(id)
    if artista:
        artista.nome = dados['nome']
        db.session.commit()
        return artista


def delete_artista(id):
    artista = get_artista_by_id(id)
    if artista:
        delete(artista)
        return artista


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

from .. import db
from ..model.Genero import Genero


def add_genero(dados):
    genero = Genero.query.filter_by(tipo=dados['tipo']).first()
    if not genero:
        novo_genero = Genero(
            tipo=dados['tipo'],
        )
        save(novo_genero)
        return novo_genero


def get_all_generos():
    generos = Genero.query.all()
    return generos


def get_genero_by_id(id):
    genero = Genero.query.get(id)
    return genero


def get_genero_by_tipo(tipo):
    genero = Genero.query.filter_by(tipo=tipo).first()
    return genero


def update_genero(id, dados):
    genero = get_genero_by_id(id)
    if genero:
        genero.tipo = dados['tipo']
        db.session.commit()
        return genero


def delete_genero(id):
    genero = get_genero_by_id(id)
    if genero:
        delete(genero)
        return genero


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

from .. import db
from ..model.Sala import Sala


def add_sala(dados):
    sala = Sala.query.filter_by(numero=dados['numero']).first()
    if not sala:
        nova_sala = Sala(
            numero=dados['numero'],
            total_assentos=dados['total_assentos']
        )
        save(nova_sala)
        return nova_sala


def get_all_salas():
    salas = Sala.query.all()
    return salas


def get_sala_by_id(id):
    sala = Sala.query.get(id)
    return sala


def get_sala_by_numero(numero):
    sala = Sala.query.filter_by(numero=numero).first()
    return sala


def update_sala(id, dados):
    sala = get_sala_by_id(id)
    if sala:
        sala.numero = dados['numero']
        sala.assentos = dados['assentos']
        db.session.commit()
    return sala


def delete_sala(id):
    sala = get_sala_by_id(id)
    if sala:
        delete(sala)
    return sala


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

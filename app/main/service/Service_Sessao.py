from datetime import datetime

from .. import db
from ..model.Sessao import Sessao

from ..service.Service_Filme import get_filme_by_titulo
from ..service.Service_Sala import get_sala_by_numero


def add_sessao(dados):
    filme = get_filme_by_titulo(dados['titulo'])
    sala = get_sala_by_numero(dados['numero'])
    sessao = Sessao.query.filter(
        Sessao.data == dados['data'],
        Sessao.horario == dados['horario'],
        Sessao.sala_id == sala.id
    ).first()
    if filme and sala and not sessao:
        nova_sessao = Sessao(
            data=datetime.strptime(dados['data'], '%Y/%m/%d'),
            horario=dados['horario'],
            total_tickets=sala.total_assentos
        )
        nova_sessao.filme = filme
        nova_sessao.sala = sala
        save(nova_sessao)
        return nova_sessao


def get_all_sessoes():
    sessoes = Sessao.query.all()
    return sessoes


def get_sessao_by_id(id):
    sessao = Sessao.query.filter_by(id=id).first()
    return sessao


def update_sessao(id, dados):
    pass


def delete_sessao(id):
    pass


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

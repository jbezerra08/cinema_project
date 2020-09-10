from datetime import datetime

from main import db
from main.model import Sessao
from main.model.Filme import Filme
from main.model.Sala import Sala

from main.service.Service_Filme import get_filme_by_titulo
from main.service.Service_Sala import get_sala_by_numero


def add_sessao(dados):
    filme = get_filme_by_titulo(dados['titulo'])
    sala = get_sala_by_numero(dados['numero'])
    sessao = Sessao.query.filter(
        Sessao.data == dados['data'],
        Sessao.horario == dados['horario'],
        Sessao.sala_id == sala.id
    ).first()
    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Filme não está cadastrado.'
        }
        return resposta, 409
    if not Sala:
        resposta = {
            'status': 'falha',
            'message': 'Sala não está cadastrada.'
        }
        return resposta, 409
    if not sessao:
        nova_sessao = Sessao(
            data=datetime.strptime(dados['data'], '%Y/%m/%d'),
            horario=dados['horario'],
            total_tickets=sala.total_assentos
        )
        nova_sessao.filme = filme
        nova_sessao.sala = sala
        save(nova_sessao)
        resposta = {
            'status': 'sucesso',
            'message': f'Nova sessão em {nova_sessao.data} as {nova_sessao.horario}.'
        }
        return resposta, 200
    resposta = {
        'status': 'falha',
        'message': f'Horário para a sala {sala.numero} previamente cadastrado em outra sessão.'
    }
    return resposta, 409


def get_all_sessoes():
    sessoes = Sessao.query.all()
    return sessoes


def get_sessao_by_id(id):
    sessao = Sessao.query.filter_by(id=id).first()
    return sessao


def update_sessao(dados):
    pass


def delete_sessao(id):
    pass


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

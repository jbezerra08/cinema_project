from datetime import datetime

from .. import db
from ..model.Sessao import Sessao

from ..service.Service_Filme import get_filme_by_titulo
from ..service.Service_Sala import get_sala_by_numero


def add_sessao(dados):
    filme = get_filme_by_titulo(dados['titulo'])
    sala = get_sala_by_numero(dados['numero'])
    sessao = Sessao.query.filter(
                    Sessao.sala_id == sala.id,
                    Sessao.data == datetime.strptime(dados['data'], '%Y/%m/%d').date(),
                    Sessao.horario == dados['horario']
                    ).first()
    if filme and sala and not sessao:
        nova_sessao = Sessao(
            data=datetime.strptime(dados['data'], '%Y/%m/%d').date(),
            horario=dados['horario'],
            total_tickets=sala.total_assentos,
            preco=dados['preco']
        )
        nova_sessao.filme = filme
        nova_sessao.sala = sala
        save(nova_sessao)
        return nova_sessao


def get_all_sessoes():
    sessoes = Sessao.query.all()
    return sessoes


def get_sessao_by_id(id):
    sessao = Sessao.query.get(id)
    return sessao


# apenas tickets -> cada compra reduz o total disponivel
# caso ocorra algum erro no cadastro da sessão é necessário apagar o registro e cadastrar novamente
def update_tickets_sessao(id, quantidade_comprada):
    sessao = get_sessao_by_id(id)
    if sessao:
        sessao.total_tickets -= quantidade_comprada
        db.session.commit()
        return sessao


def delete_sessao(id):
    sessao = get_sessao_by_id(id)
    if sessao:
        delete(sessao)
        return sessao


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

from .. import db
from ..model.Ticket import Ticket

from ..service.Service_Usuario import get_usuario_by_email
from ..service.Service_Sessao import get_sessao_by_id, update_tickets_sessao


def add_ticket(dados):
    sessao = get_sessao_by_id(dados['id'])
    usuario = get_usuario_by_email(dados['email'])
    if sessao and usuario and sessao.total_tickets >= dados['quantidade_comprada']:
        novo_ticket = Ticket(
            total_pago=sessao.preco * dados['quantidade_comprada'],
            validade=sessao.data
        )
        novo_ticket.sessao = sessao
        novo_ticket.usuario = usuario
        save(novo_ticket)
        update_tickets_sessao(sessao.id, dados['quantidade_comprada'])
        return novo_ticket


def get_all_tickets():
    tickets = Ticket.query.all()
    return tickets


def get_ticket_by_id(id):
    ticket = Ticket.query.get(id)
    return ticket


def update_ticket(id, dados):
    pass


def delete_ticket(id):
    ticket = get_ticket_by_id(id)
    if ticket:
        delete(ticket)
        return ticket


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

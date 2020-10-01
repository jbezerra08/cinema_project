from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..service import Service_Ticket
from ..model.Ticket import ticket_schema, tickets_schema

ticket_blueprint = Blueprint('tickets', __name__)


@ticket_blueprint.route(
    '/tickets',
    methods=['GET']
)
@jwt_required
def get_tickets():
    tickets = Service_Ticket.get_all_tickets()

    if not tickets:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return tickets_schema.jsonify(tickets), 200


@ticket_blueprint.route(
    '/tickets/<int:ticket_id>',
    methods=['GET']
)
@jwt_required
def get_ticket(ticket_id):
    ticket = Service_Ticket.get_ticket_by_id(ticket_id)

    if not ticket:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return ticket_schema.jsonify(ticket), 200


@ticket_blueprint.route(
    '/tickets',
    methods=['POST']
)
@jwt_required
def create_ticket():
    ticket = Service_Ticket.add_ticket(request.get_json())

    if not ticket:
        resposta = {
            'status': 'falha',
            'message': 'Erro ao processar requisição.'
        }
        return jsonify(resposta), 409

    return ticket_schema.jsonify(ticket), 201


@ticket_blueprint.route(
    '/tickets/<int:ticket_id>',
    methods=['DELETE']
)
@jwt_required
def delete_ticket(ticket_id):
    ticket = Service_Ticket.delete_ticket(ticket_id)

    if not ticket:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return ticket_schema.jsonify(ticket), 200

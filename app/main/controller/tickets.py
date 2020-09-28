from flask import request, Blueprint
from ..service import Service_Ticket
from ..model.Ticket import ticket_schema, tickets_schema

ticket_blueprint = Blueprint("tickets", __name__)


@ticket_blueprint.route("/tickets", methods=["GET"])
def get_tickets():
    return tickets_schema.jsonify(Service_Ticket.get_all_tickets())

@ticket_blueprint.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    return ticket_schema.jsonify(Service_Ticket.get_ticket)


@ticket_blueprint.route("/tickets", methods=["POST"])
def create_ticket():
    return ticket_schema.jsonify(Service_Ticket.add_ticket(request.get_json()))


@ticket_blueprint.route("/tickets/<int:ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    return ticket_schema.jsonify(Service_Ticket.update_ticket(ticket_id, request.get_json()))


@ticket_blueprint.route("/tickets/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    return ticket_schema.jsonify(Service_Ticket.delete_ticket(ticket_id))
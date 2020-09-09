import datetime

from main import db
from main.model import Ticket


def add_ticket(dados):
    pass


def get_all_tickets():
    pass


def get_ticket(id):
    pass


def update_ticket(id):
    pass


def delete_ticket(id):
    pass


def save(dados):
    db.session.add(dados)
    db.session.commit()

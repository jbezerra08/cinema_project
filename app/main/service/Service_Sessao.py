from datetime import datetime

from main import db
from main.model import Sessao


def add_sessao(dados):
    pass


def get_all_sessoes():
    pass


def get_sessoes(id):
    pass


def update_sessao(id):
    pass


def delete_sessao(id):
    pass


def save(dados):
    db.session.add(dados)
    db.session.commit()

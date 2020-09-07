import datetime

from app.main import db
from app.main.model import Ticket


# salva um ticket no banco de dados
def save_ticket(dados):
    pass


# devolve todos os tickets salvos no banco de dados
def get_all_tickets():
    pass


# devolve um ticket a partir do seu id
def get_ticket(id):
    pass


# atualiza/edita um ticket
def update_ticket(id):
    pass


# deleta um ticket a partir do seu id
def delete_ticket(id):
    pass


# função auxiliar para salvar no banco de dados
def save(dados):
    db.session.add(dados)
    db.session.commit()

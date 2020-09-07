import datetime

from app.main import db
from app.main.model import Sessao


# salva uma sessao no banco de dados
def save_sessao(dados):
    pass


# devolve todos as sessões salvas no banco de dados
def get_all_sessoes():
    pass


# devolve um sessoes a partir do seu id
def get_sessoes(id):
    pass


# atualiza/edita uma sessao
def update_sessao(id):
    pass


# deleta um sessao a partir do seu id
def delete_sessao(id):
    pass


# função auxiliar para salvar no banco de dados
def save(dados):
    db.session.add(dados)
    db.session.commit()

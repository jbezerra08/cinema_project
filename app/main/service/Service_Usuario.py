import uuid
import datetime

from app.main import db
from app.main.model import Usuario


# salva um usuário no banco de dados
def save_usuario(dados):
    pass


# devolve todos os usuários salvos no banco de dados
def get_all_usuarios():
    pass


# devolve um usuário a partir do seu id público
def get_usuario(public_id):
    pass


# atualiza/edita um usuario
def update_usuario(id):
    pass


# deleta um usuario a partir do seu id
def delete_usuario(id):
    pass


# função auxiliar para salvar no banco de dados
def save(dados):
    db.session.add(dados)
    db.session.commit()

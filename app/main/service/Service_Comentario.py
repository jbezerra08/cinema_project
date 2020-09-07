from app.main import db
from app.main.model import Ticket


# salva um comentario no banco de dados
def save_comentario(dados):
    pass


# devolve todos os comentarios salvos no banco de dados
def get_all_comentarios():
    pass


# devolve um comentario a partir do seu id
def get_comentario(id):
    pass


# atualiza/edita um comentario
def update_comentario(id):
    pass


# deleta um comentario a partir do seu id
def delete_comentario(id):
    pass


# função auxiliar para salvar no banco de dados
def save(dados):
    db.session.add(dados)
    db.session.commit()

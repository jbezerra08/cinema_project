from app.main import db
from app.main.model import Filme


# salva um filme no banco de dados
def save_filme(dados):
    pass


# devolve todos os filmes salvos no banco de dados
def get_all_filmes():
    pass


# devolve um filme a partir do seu id
def get_filme(id):
    pass


# atualiza/edita um filme
def update_filme(id):
    pass


# deleta um filme a partir do seu id
def delete_filme(id):
    pass


# função auxiliar para salvar no banco de dados
def save(dados):
    db.session.add(dados)
    db.session.commit()

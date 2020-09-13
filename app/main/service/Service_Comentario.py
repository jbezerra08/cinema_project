from datetime import datetime
from flask import jsonify

from .. import db
from ..model.Comentario import Comentario
from ..model.Filme import Filme
from ..model.Usuario import Usuario

from .Service_Filme import get_filme_by_titulo, update_filme
from .Service_Usuario import get_usuario_by_email, update_usuario


def add_comentario(dados):
    filme = get_filme_by_titulo(dados['titulo'])
    usuario = get_usuario_by_email(dados['email'])
    if filme and usuario:
        novo_comentario = Comentario(
            data=datetime.utcnow(),
            texto_comentario=dados['texto_comentario'],
        )
        novo_comentario.usuario = usuario
        novo_comentario.filme = filme
        save(novo_comentario)
        return novo_comentario


def get_all_comentarios():
    comentarios = Comentario.query.all()
    return comentarios


def get_comentarios_by_id(dados):
    comentario = Comentario.query.get(dados['id'])
    return comentario


def get_comentarios_by_filme(dados):
    filme = get_filme_by_titulo(dados['titulo'])
    comentarios = Comentario.query.with_parent(filme).order_by(Comentario.data).all()
    return comentarios


def get_comentarios_by_usuario(dados):
    usuario = get_usuario_by_email(dados['email'])
    comentarios = Comentario.query.with_parent(usuario).order_by(Comentario.data).all()
    return comentarios


# usuario atualiza um comentário em um filme
def update_comentario(dados):
    pass


# usuario deleta um comentário em um filme
def delete_comentario(dados):
    pass


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

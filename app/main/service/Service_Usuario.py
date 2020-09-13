from datetime import datetime

from .. import db
from ..model.Usuario import Usuario


def add_usuario(dados):
    usuario = Usuario.query.filter_by(email=dados['email']).first()
    if not usuario:
        novo_usuario = Usuario(
            nome=dados['nome'],
            sobrenome=dados['sobrenome'],
            email=dados['email'],
            senha=dados['senha'],
            data_cadastro=datetime.utcnow()
        )
        save(novo_usuario)
        return novo_usuario


def get_all_usuarios():
    usuarios = Usuario.query.all()
    return usuarios


def get_usuario_by_id(id):
    usuario = Usuario.query.get(id)
    return usuario


def get_usuario_by_email(email):
    usuario = Usuario.query.filter_by(email=email).first()
    return usuario


def update_usuario(id, dados):
    usuario = get_usuario_by_id(id)
    if usuario:
        usuario.nome = dados['nome']
        usuario.sobrenome = dados['sobrenome']
        usuario.email = dados['email']
        db.session.commit()
    return usuario


def delete_usuario(id):
    usuario = get_usuario_by_id(id)
    if usuario:
        delete(usuario)
    return usuario


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

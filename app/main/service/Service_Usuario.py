from datetime import datetime

from main import db
from main.model.Usuario import Usuario


def add_usuario(dados):
    usuario = Usuario.query.filter_by(email=dados['email']).first()
    if not usuario:
        novo_usuario = Usuario(
            nome=dados['nome'],
            email=dados['email'],
            senha=dados['senha'],
            registered_on=datetime.utcnow()
        )
        save(novo_usuario)
        resposta = {
            'status': 'successo',
            'message': 'Registro adicionado com sucesso.'
        }
        return resposta, 201
    else:
        resposta = {
            'status': 'falha',
            'message': 'Usuário já está cadastrado.'
        }
        return resposta, 409


def get_all_usuarios():
    usuarios = Usuario.query.all()
    return usuarios


def get_usuario_by_id(dados):
    usuario = Usuario.query.get(dados['id'])
    return usuario


def get_usuario_by_nome(nome):
    usuario = Usuario.query.filter_by(nome=nome).first()
    return usuario


def update_usuario(dados):
    usuario = get_usuario_by_id(dados['id'])
    if not usuario:
        resposta = {
            'status': 'falha',
            'message': 'Usuário não existe.'
        }
        return resposta, 404
    else:
        usuario.nome = dados['nome']
        usuario.email = dados['email']
        usuario.comentarios.append(dados['texto_comentario'])
        db.session.commit()
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do usuário atualizados.'
        }
    return resposta, 200


def delete_usuario(id):
    usuario = get_usuario_by_id(dados['id'])
    if not usuario:
        resposta = {
            'status': 'falha',
            'message': 'Usuário não existe.'
        }
        return resposta, 404
    else:
        delete(usuario)
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do usuário removidos.'
        }
    return resposta, 200


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

from main import db
from main.model.Genero import Genero


def add_genero(dados):
    genero = Genero.query.filter_by(tipo=dados['tipo']).first()
    if not genero:
        novo_genero = Genero(
            tipo=dados['tipo'],
        )
        save(novo_genero)
        resposta = {
            'status': 'successo',
            'message': 'Registro adicionado com sucesso.'
        }
        return resposta, 201
    else:
        resposta = {
            'status': 'falha',
            'message': 'Genero já está cadastrado.'
        }
        return resposta, 409


def get_all_generos():
    generos = Genero.query.all()
    return generos


def get_genero_by_id(id):
    genero = Genero.query.get(id)
    return genero


def get_genero_by_tipo(tipo):
    genero = Genero.query.filter_by(tipo=tipo).first()
    return genero


def update_genero(dados):
    genero = get_genero_by_id(dados['id'])
    if not genero:
        resposta = {
            'status': 'falha',
            'message': 'Genero não existe.'
        }
        return resposta, 404
    else:
        genero.tipo = dados['tipo']
        db.session.commit()
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do Genero atualizados.'
        }
    return resposta, 200


def delete_genero(id):
    genero = get_genero_by_id(dados['id'])
    if not genero:
        resposta = {
            'status': 'falha',
            'message': 'Genero não existe.'
        }
        return resposta, 404
    else:
        delete(genero)
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do Genero removidos.'
        }
    return resposta, 200


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

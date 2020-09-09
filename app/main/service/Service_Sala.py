from main import db
from main.model.Sala import Sala


def add_sala(dados):
    sala = Sala.query.filter_by(numero=dados['numero']).first()
    if not sala:
        nova_sala = Sala(
            numero=dados['numero'],
            total_assentos=dados['total_assentos']
        )
        save(nova_sala)
        resposta = {
            'status': 'successo',
            'message': 'Registro adicionado com sucesso.'
        }
        return resposta, 201
    else:
        resposta = {
            'status': 'falha',
            'message': 'Sala já está cadastrada.'
        }
        return resposta, 409


def get_all_salas():
    salas = Sala.query.all()
    return salas


def get_sala_by_id(id):
    sala = Sala.query.get(id)
    return sala


def update_sala(dados):
    sala = get_sala_by_id(dados['id'])
    if not sala:
        resposta = {
            'status': 'falha',
            'message': 'Sala não existe.'
        }
        return resposta, 404
    else:
        sala.numero = dados['numero']
        sala.assentos = dados['assentos']
        db.session.commit()
        resposta = {
            'status': 'sucesso',
            'message': 'Dados da sala atualizados.'
        }
    return resposta, 200


def delete_sala(id):
    sala = get_sala_by_id(id)
    if not sala:
        resposta = {
            'status': 'falha',
            'message': 'Sala não existe.'
        }
        return resposta, 404
    else:
        delete(sala)
        resposta = {
            'status': 'sucesso',
            'message': 'Dados da sala removidos.'
        }
    return resposta, 200


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

from main import db
from main.model.Artista import Artista


def add_artista(dados):
    artista = Artista.query.filter_by(nome=dados['nome']).first()
    if not artista:
        novo_artista = Artista(
            nome=dados['nome'],
        )
        save(novo_artista)
        resposta = {
            'status': 'successo',
            'message': 'Registro adicionado com sucesso.'
        }
        return resposta, 201
    else:
        resposta = {
            'status': 'falha',
            'message': 'Artista já está cadastrado.'
        }
        return resposta, 409


def get_all_artistas():
    artistas = Artista.query.all()
    return artistas


def get_artista_by_id(id):
    artista = Artista.query.get(id)
    return artista


def get_artista_by_nome(nome):
    artista = Artista.query.filter_by(nome=nome).first()
    return artista


def update_artista(dados):
    artista = get_artista_by_id(dados['id'])
    if not artista:
        resposta = {
            'status': 'falha',
            'message': 'Artista não existe.'
        }
        return resposta, 404
    else:
        artista.nome = dados['nome']
        db.session.commit()
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do artista atualizados.'
        }
    return resposta, 200


def delete_artista(id):
    artista = get_artista_by_id(dados['id'])
    if not artista:
        resposta = {
            'status': 'falha',
            'message': 'Artista não existe.'
        }
        return resposta, 404
    else:
        delete(artista)
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do artista removidos.'
        }
    return resposta, 200


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

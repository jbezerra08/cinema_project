from datetime import datetime

from main import db
from main.model.Filme import Filme
from main.service.Service_Genero import get_genero_by_tipo
from main.service.Service_Artista import get_artista_by_nome


# adiciona apenas os generos e artistas previamente cadastrados
def add_filme(dados):
    filme = Filme.query.filter_by(titulo=dados['titulo']).first()
    if not filme:
        novo_filme = Filme(
            titulo=dados['titulo'],
            lancamento=datetime.strptime(dados['lancamento'], '%Y/%m/%d'),
            duracao=dados['duracao'],
            registered_on=datetime.utcnow(),
            sinopse=dados['sinopse'],
            enredo=dados['enredo']
        )
        [novo_filme.generos.append(obj) for obj in
            [get_genero_by_tipo(genero) for genero in dados['generos']]]
        [novo_filme.elenco.append(obj) for obj in
            [get_artista_by_nome(artista) for artista in dados['elenco']]]
        save(novo_filme)
        resposta = {
            'status': 'successo',
            'message': 'Registro adicionado com sucesso.'
        }
        return resposta, 201
    else:
        resposta = {
            'status': 'falha',
            'message': 'Filme já está cadastrado.'
        }
        return resposta, 409


def get_all_filmes():
    filmes = Filmes.query.all()
    return filmes


def get_filme_by_id(dados):
    filme = Filme.query.get(dados['id'])
    return filme


def get_filme_by_titulo(titulo):
    filme = Filme.query.filter_by(titulo=titulo).first()
    return filme


def update_filme(dados):
    filme = get_filme_by_id(dados['id'])
    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Filme não existe.'
        }
        return resposta, 404
    else:
        filme.titulo = dados['titulo']
        filme.lancamento = dados['lancamento']
        filme.duracao = dados['duracao']
        filme.sinopse = dados['sinopse']
        filme.enredo = dados['enredo']
        filme.comentarios.append(dados['texto_comentario'])
        db.session.commit()
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do filme atualizados.'
        }
    return resposta, 200


def delete_filme(id):
    filme = get_filme_by_id(id)
    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Filme não existe.'
        }
        return resposta, 404
    else:
        delete(filme)
        resposta = {
            'status': 'sucesso',
            'message': 'Dados do filme removidos.'
        }
    return resposta, 200


def save(dados):
    db.session.add(dados)
    db.session.commit()


def delete(dados):
    db.session.delete(dados)
    db.session.commit()

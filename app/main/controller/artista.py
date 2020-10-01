from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..service import Service_Artista
from ..model.Artista import artista_schema, artistas_schema

artista_blueprint = Blueprint('artistas', __name__)


@artista_blueprint.route(
    '/artistas',
    methods=['GET']
)
@jwt_required
def get_artistas():
    artistas = Service_Artista.get_all_artistas()

    if not artistas:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return artistas_schema.jsonify(artistas), 200


@artista_blueprint.route(
    '/artistas/<int:artista_id>',
    methods=['GET']
)
@jwt_required
def get_artista(artista_id):
    artista = Service_Artista.get_artista_by_id(artista_id)

    if not artista:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return artista_schema.jsonify(artista), 200


@artista_blueprint.route(
    '/artistas/<artista_nome>',
    methods=['GET']
)
@jwt_required
def get_artista_nome(artista_nome):
    artista = Service_Artista.get_artista_by_nome(artista_nome)

    if not artista:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return artista_schema.jsonify(artista), 200


@artista_blueprint.route(
    '/artistas',
    methods=['POST']
)
@jwt_required
def create_artista():
    artista = Service_Artista.add_artista(request.get_json())

    if not artista:
        resposta = {
            'status': 'falha',
            'message': 'Registro já existe.'
        }
        return jsonify(resposta), 409

    return artista_schema.jsonify(artista), 201


@artista_blueprint.route(
    '/artistas/<int:artista_id>',
    methods=['PUT']
)
@jwt_required
def update_artista(artista_id):
    artista = Service_Artista.update_artista(artista_id, request.get_json())

    if not artista:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return artista_schema.jsonify(artista), 200


@artista_blueprint.route(
    '/artistas/<int:artista_id>',
    methods=['DELETE']
)
@jwt_required
def delete_artista(artista_id):
    artista = Service_Artista.delete_artista(artista_id)

    if not artista:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return artista_schema.jsonify(artista), 200

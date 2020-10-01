from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from ..service import Service_Filme
from ..model.Filme import filme_schema, filmes_schema

filme_blueprint = Blueprint('filmes', __name__)


@filme_blueprint.route(
    '/filmes',
    methods=['GET']
)
def get_filmes():
    filmes = Service_Filme.get_all_filmes()

    if not filmes:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return filmes_schema.jsonify(filmes), 200


@filme_blueprint.route(
    '/filmes/<int:id_filme>',
    methods=['GET']
)
def get_filme(id_filme):
    filme = Service_Filme.get_filme_by_id(id_filme)

    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return filme_schema.jsonify(filme), 200


@filme_blueprint.route(
    '/filmes/<titulo_filme>',
    methods=['GET']
)
def get_filme_by_titulo(titulo_filme):
    filme = Service_Filme.get_filme_by_titulo(titulo_filme)

    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return filme_schema.jsonify(filme), 200


@filme_blueprint.route(
    '/filmes',
    methods=['POST']
)
@jwt_required
def create_filme():
    filme = Service_Filme.add_filme(request.get_json())

    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Registro já existe.'
        }
        return jsonify(resposta), 409

    return filme_schema.jsonify(filme), 201


@filme_blueprint.route(
    '/filmes/<int:filme_id>',
    methods=['PUT']
)
@jwt_required
def update_filme(filme_id):
    filme = Service_Filme.update_filme(filme_id, request.get_json())

    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return filme_schema.jsonify(filme), 200


@filme_blueprint.route(
    '/filmes/<int:filme_id>',
    methods=['DELETE']
)
@jwt_required
def delete_filme(filme_id):
    filme = Service_Filme.delete_filme(filme_id)

    if not filme:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return filme_schema.jsonify(filme), 200

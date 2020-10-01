from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..service import Service_Genero
from ..model.Genero import genero_schema, generos_schema

genero_blueprint = Blueprint('generos', __name__)


@genero_blueprint.route(
    '/generos',
    methods=['GET']
)
@jwt_required
def get_generos():
    generos = Service_Genero.get_all_generos()

    if not generos:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return generos_schema.jsonify(generos), 200


@genero_blueprint.route(
    '/generos/<int:genero_id>',
    methods=['GET']
)
@jwt_required
def get_genero(genero_id):
    genero = Service_Genero.get_genero_by_id(genero_id)

    if not genero:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return genero_schema.jsonify(genero), 200


@genero_blueprint.route(
    '/generos/<genero_tipo>',
    methods=['GET']
)
@jwt_required
def get_genero_by_tipo(genero_tipo):
    genero = Service_Genero.get_genero_by_tipo(genero_tipo)

    if not genero:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return genero_schema.jsonify(genero), 200


@genero_blueprint.route(
    '/generos',
    methods=['POST']
)
@jwt_required
def create_genero():
    genero = Service_Genero.add_genero(request.get_json())

    if not genero:
        resposta = {
            'status': 'falha',
            'message': 'Registro já existe.'
        }
        return jsonify(resposta), 409

    return genero_schema.jsonify(genero), 201


@genero_blueprint.route(
    '/generos/<int:genero_id>',
    methods=['PUT']
)
@jwt_required
def update_genero(genero_id):
    genero = Service_Genero.update_genero(genero_id, request.get_json())

    if not genero:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return genero_schema.jsonify(genero), 200


@genero_blueprint.route(
    '/generos/<int:genero_id>',
    methods=['DELETE']
)
@jwt_required
def delete_genero(genero_id):
    genero = Service_Genero.delete_genero(genero_id)

    if not genero:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return genero_schema.jsonify(genero), 200

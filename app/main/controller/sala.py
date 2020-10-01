from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..service import Service_Sala
from ..model.Sala import sala_schema, salas_schema

sala_blueprint = Blueprint('salas', __name__)


@sala_blueprint.route(
    '/salas',
    methods=['GET']
)
@jwt_required
def get_salas():
    salas = Service_Sala.get_all_salas()

    if not salas:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return salas_schema.jsonify(salas), 200


@sala_blueprint.route(
    '/salas/<int:sala_id>',
    methods=['GET']
)
@jwt_required
def get_sala(sala_id):
    sala = Service_Sala.get_sala_by_id(sala_id)

    if not sala:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return sala_schema.jsonify(sala), 200


@sala_blueprint.route(
    '/salas',
    methods=['POST']
)
@jwt_required
def create_sala():
    sala = Service_Sala.add_sala(request.get_json())

    if not sala:
        resposta = {
            'status': 'falha',
            'message': 'Registro já existe.'
        }
        return jsonify(resposta), 409

    return sala_schema.jsonify(sala), 201


@sala_blueprint.route(
    '/salas/<int:sala_id>',
    methods=['PUT']
)
@jwt_required
def update_sala(sala_id):
    sala = Service_Sala.update_sala(sala_id, request.get_json())

    if not sala:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return sala_schema.jsonify(sala), 200


@sala_blueprint.route(
    '/salas/<int:sala_id>',
    methods=['DELETE']
)
@jwt_required
def delete_sala(sala_id):
    sala = Service_Sala.delete_sala(sala_id)

    if not sala:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return sala_schema.jsonify(sala), 200

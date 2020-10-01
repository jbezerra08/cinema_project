from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..service import Service_Comentario
from ..model.Comentario import comentario_schema, comentarios_schema

comentario_blueprint = Blueprint('comentarios', __name__)


@comentario_blueprint.route(
    '/comentarios',
    methods=['GET']
)
@jwt_required
def get_comentarios():
    comentarios = Service_Comentario.get_all_comentarios()

    if not comentarios:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return comentarios_schema.jsonify(comentarios), 200


@comentario_blueprint.route(
    '/comentarios/<int:comentario_id>',
    methods=['GET']
)
@jwt_required
def get_comentario(comentario_id):
    comentario = Service_Comentario.get_comentario_by_id(comentario_id)

    if not comentario:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return comentario_schema.jsonify(comentario), 200


@comentario_blueprint.route(
    '/comentarios/filme',
    methods=['GET']
)
@jwt_required
def get_comentario_by_filme():
    comentarios = Service_Comentario.get_comentarios_by_filme(request.get_json())

    if not comentarios:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return comentarios_schema.jsonify(comentarios), 200


@comentario_blueprint.route(
    '/comentarios/usuario',
    methods=['GET']
)
@jwt_required
def get_comentario_by_usuario():
    comentarios = Service_Comentario.get_comentarios_by_usuario(request.get_json())

    if not comentarios:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return comentarios_schema.jsonify(comentarios), 200


@comentario_blueprint.route(
    '/comentarios',
    methods=['POST']
)
@jwt_required
def create_comentario():
    comentario = Service_Comentario.add_comentario(request.get_json())

    if not comentario:
        resposta = {
            'status': 'falha',
            'message': 'Erro ao processar requisição.'
        }
        return jsonify(resposta), 409

    return comentario_schema.jsonify(comentario), 201


@comentario_blueprint.route(
    '/comentarios',
    methods=['PUT']
)
@jwt_required
def update_comentario():
    comentario = Service_Comentario.update_comentario(request.get_json())

    if not comentario:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return comentario_schema.jsonify(comentario), 200


@comentario_blueprint.route(
    '/comentarios',
    methods=['DELETE']
)
@jwt_required
def delete_comentario():
    comentario = Service_Comentario.delete_comentario(request.get_json())

    if not comentario:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return comentario_schema.jsonify(comentario), 200

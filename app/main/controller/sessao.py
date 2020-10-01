from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..service import Service_Sessao
from ..model.Sessao import sessao_schema, sessoes_schema

sessao_blueprint = Blueprint('sessoes', __name__)


@sessao_blueprint.route(
    '/sessoes',
    methods=['GET']
)
@jwt_required
def get_sessoes():
    sessoes = Service_Sessao.get_all_sessoes()

    if not sessoes:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return sessoes_schema.jsonify(sessoes), 200


@sessao_blueprint.route(
    '/sessoes/<int:sessao_id>',
    methods=['GET']
)
@jwt_required
def get_sessao(sessao_id):
    sessao = Service_Sessao.get_sessao_by_id(sessao_id)

    if not sessao:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return sessao_schema.jsonify(sessao), 200


@sessao_blueprint.route(
    '/sessoes',
    methods=['POST']
)
@jwt_required
def create_sessao():
    sessao = Service_Sessao.add_sessao(request.get_json())

    if not sessao:
        resposta = {
            'status': 'falha',
            'message': 'Registro já existe.'
        }
        return jsonify(resposta), 409

    return sessao_schema.jsonify(sessao), 201


@sessao_blueprint.route(
    '/sessoes/<int:sessao_id>',
    methods=['PUT']
)
@jwt_required
def update_sessao(sessao_id):
    sessao = Service_Sessao.update_sessao(sessao_id, request.get_json())

    if not sessao:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return sessao_schema.jsonify(sessao), 200


@sessao_blueprint.route(
    '/sessoes/<int:sessao_id>',
    methods=['DELETE']
)
@jwt_required
def delete_sessao(sessao_id):
    sessao = Service_Sessao.delete_sessao(sessao_id)

    if not sessao:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return sessao_schema.jsonify(sessao), 200

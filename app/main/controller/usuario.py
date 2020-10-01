import datetime
from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required
from ..service import Service_Usuario
from ..model.Usuario import usuario_schema, usuarios_schema

usuario_blueprint = Blueprint('usuarios', __name__)


@usuario_blueprint.route(
    '/usuarios',
    methods=['GET']
)
@jwt_required
def get_usuarios():
    usuarios = Service_Usuario.get_all_usuarios()

    if not usuarios:
        resposta = {
            'status': 'falha',
            'message': 'Não existem registros no sistema'
        }
        return jsonify(resposta), 404

    return usuarios_schema.jsonify(usuarios), 200


@usuario_blueprint.route(
    '/usuarios/<int:usuario_id>',
    methods=['GET']
)
@jwt_required
def get_usuario(usuario_id):
    usuario = Service_Usuario.get_usuario_by_id(usuario_id)

    if not usuario:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return usuario_schema.jsonify(usuario), 200


@usuario_blueprint.route(
    '/usuarios',
    methods=['POST']
)
def create_usuario():
    usuario = Service_Usuario.add_usuario(request.get_json())

    if not usuario:
        resposta = {
            'status': 'falha',
            'message': 'Registro já existe.'
        }
        return jsonify(resposta), 409

    return usuario_schema.jsonify(usuario), 201


@usuario_blueprint.route(
    '/usuarios/login',
    methods=['POST']
)
def login_usuario():
    body = request.get_json()
    usuario = Service_Usuario.get_usuario_by_email(body.get('email'))
    authorized = usuario.verificar_senha(senha=body.get('senha'))

    if not authorized:
        resposta = {
            'status': 'falha',
            'message': 'Email ou Senha inválidos.'
        }
        return jsonify(resposta), 401

    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(usuario.id), expires_delta=expires)
    resposta = {
            'status': 'sucesso',
            'token': access_token
        }
    return jsonify(resposta), 200


@usuario_blueprint.route(
    '/usuarios/<int:usuario_id>',
    methods=['PUT']
)
@jwt_required
def update_usuario(usuario_id):
    usuario = Service_Usuario.update_usuario(usuario_id, request.get_json())

    if not usuario:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return usuario_schema.jsonify(usuario), 200


@usuario_blueprint.route(
    '/usuarios/<int:usuario_id>',
    methods=['DELETE']
)
@jwt_required
def delete_usuario(usuario_id):
    usuario = Service_Usuario.delete_usuario(usuario_id)

    if not usuario:
        resposta = {
            'status': 'falha',
            'message': 'Registro não encontrado no sistema.'
        }
        return jsonify(resposta), 404

    return usuario_schema.jsonify(usuario), 200

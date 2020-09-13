from flask import request, Blueprint
from ..service import Service_Usuario
from ..model.Usuario import usuario_schema, usuarios_schema

usuario_blueprint = Blueprint('usuarios', __name__)


@usuario_blueprint.route("/usuarios", methods=["GET"])
def get_usuarios():
    return usuarios_schema.jsonify(Service_Usuario.get_all_usuarios())


@usuario_blueprint.route("/usuarios/<int:usuario_id>", methods=["GET"])
def get_usuario(usuario_id):
    return usuario_schema.jsonify(Service_Usuario.get_usuario_by_id(usuario_id))


@usuario_blueprint.route("/usuarios", methods=["POST"])
def create_usuario():
    return usuario_schema.jsonify(Service_Usuario.add_usuario(request.get_json()))


@usuario_blueprint.route("/usuarios/<int:usuario_id>", methods=["PUT"])
def update_usuario(usuario_id):
    return usuario_schema.jsonify(Service_Usuario.update_usuario(usuario_id, request.get_json()))


@usuario_blueprint.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
def delete_usuario(usuario_id):
    return usuario_schema.jsonify(Service_Usuario.delete_usuario(usuario_id))

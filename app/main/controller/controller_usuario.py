from flask import Flask, jsonify, request, abort
from main.service import Service_Usuario


@blueprint.errorhandler(404)
def not_found(error):
    print("error", error)
    return jsonify({"error": "Not found"}), 404


@blueprint.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(Service_Usuario.get_all_usuarios)


@blueprint.route("/usuarios/<int:usuario_id>", methods=["GET"])
def get_usuario(usuario_id):
    if Service_Usuario.get_usuario_by_id(usuario_id) == None:
        abort(404)
    return jsonify(Service_Usuario.get_usuario_by_id(usuario_id))


@blueprint.route("/usuarios", methods=["POST"])
def create_usuario():
    Service_Usuario.add_usuario(dados)


@blueprint.route("/usuarios/<int:usuario_id>", methods=["PATCH"])
def update_usuario(usuario_id):
    Service_Usuario.update_usuario(usuario_id)


@blueprint.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
def delete_usuario(usuario_id):
    Service_Usuario.delete_usuario(usuario_id)
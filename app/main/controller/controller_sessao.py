from flask import Flask, jsonify, request, abort
from main.service import Service_Sessao


@blueprint.errorhandler(404)
def not_found(error):
    print("error", error)
    return jsonify({"error": "Not found"}), 404


@blueprint.route("/sessoes", methods=["GET"])
def get_sessoes():
    return jsonify(Service_Sessao.get_all_sessoes)


@blueprint.route("/sessoes/<int:sessao_id>", methods=["GET"])
def get_sessao(sessao_id):
    if Service_Sessao.get_sessao_by_id(sessao_id) == None:
        abort(404)
    return jsonify(Service_Sessao.get_sessao_by_id(sessao_id))


@blueprint.route("/sessoes", methods=["POST"])
def create_sessao():
    Service_Sessao.add_sessao(dados)


@blueprint.route("/sessoes/<int:sessao_id>", methods=["PATCH"])
def update_sessao(sessao_id):
    Service_Sessao.update_sessao(sessao_id)


@blueprint.route("/sessoes/<int:sessao_id>", methods=["DELETE"])
def delete_sessao(sessao_id):
    Service_Sessao.delete_sessao(sessao_id)
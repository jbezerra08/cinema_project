from flask import Flask, jsonify, request, abort
from main.service import Service_Sala


@blueprint.errorhandler(404)
def not_found(error):
    print("error", error)
    return jsonify({"error": "Not found"}), 404


@blueprint.route("/salas", methods=["GET"])
def get_salas():
    return jsonify(Service_Sala.get_all_salas())


@blueprint.route("/salas/<int:sala_id>", methods=["GET"])
def get_sala(sala_id):
    if Service_Sala.get_sala_by_id(sala_id) == None:
        abort(404)
    return jsonify(Service_Sala.get_sala_by_id(sala_id))


@blueprint.route("/salas", methods=["POST"])
def create_sala():
    Service_Sala.add_sala(dados)


@blueprint.route("/salas/<int:sala_id>", methods=["PATCH"])
def update_sala(sala_id):
    Service_Sala.update_sala(sala_id)


@blueprint.route("/salas/<int:sala_id>", methods=["DELETE"])
def delete_sala(sala_id):
    Service_Sala.delete_sala(sala_id)

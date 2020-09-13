from flask import request, Blueprint
from ..service import Service_Sala
from ..model.Sala import sala_schema, salas_schema

sala_blueprint = Blueprint('salas', __name__)


@sala_blueprint.route("/salas", methods=["GET"])
def get_salas():
    return salas_schema.jsonify(Service_Sala.get_all_salas())


@sala_blueprint.route("/salas/<int:sala_id>", methods=["GET"])
def get_sala(sala_id):
    return sala_schema.jsonify(Service_Sala.get_sala_by_id(sala_id))


@sala_blueprint.route("/salas", methods=["POST"])
def create_sala():
    return sala_schema.jsonify(Service_Sala.add_sala(request.get_json()))


@sala_blueprint.route("/salas/<int:sala_id>", methods=["PUT"])
def update_sala(sala_id):
    return sala_schema.jsonify(Service_Sala.update_sala(sala_id, request.get_json()))


@sala_blueprint.route("/salas/<int:sala_id>", methods=["DELETE"])
def delete_sala(sala_id):
    return sala_schema.jsonify(Service_Sala.delete_sala(sala_id))

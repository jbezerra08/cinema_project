from flask import request, Blueprint
from ..service import Service_Genero
from ..model.Genero import genero_schema, generos_schema

genero_blueprint = Blueprint("generos", __name__)


@genero_blueprint.route("/generos", methods=["GET"])
def get_generos():
    return generos_schema.jsonify(Service_Genero.get_all_generos())


@genero_blueprint.route("/generos/<int:genero_id>", methods=["GET"])
def get_genero(genero_id):
    return genero_schema.jsonify(Service_Genero.get_genero_by_id(genero_id))


@genero_blueprint.route("/generos/<str:genero_tipo>", methods=["GET"])
def get_genero_tipo(genero_tipo):
    return genero_schema.jsonify(Service_Genero.get_genero_by_tipo(genero_tipo))


@genero_blueprint.route("/generos", methods=["POST"])
def create_genero():
    return genero_schema.jsonify(Service_Genero.add_genero(request.get_json()))


@genero_blueprint.route("/generos/<int:genero_id>", methods=["PUT"])
def update_genero(genero_id):
    return genero_schema.jsonify(Service_Genero.update_genero(genero_id, request.get_json()))


@genero_blueprint.route("/generos/<int:genero_id>", methods=["DELETE"])
def delete_genero(genero_id):
    return genero_schema.jsonify(Service_Genero.delete_genero(genero_id))

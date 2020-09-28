from flask import request, Blueprint
from ..service import Service_Artista
from ..model.Artista import artista_schema, artistas_schema

artista_blueprint = Blueprint("artistas", __name__)


@artista_blueprint.route("/artistas", methods=["GET"])
def get_artistas():
    return artistas_schema.jsonify(Service_Artista.get_all_artistas())


@artista_blueprint.route("/artistas/<int:artista_id>", methods=["GET"])
def get_artista(artista_id):
    return artista_schema.jsonify(Service_Artista.get_artista_by_id)

@artista_blueprint.route("/artistas/<str:artista_nome>", methods=["GET"])
def get_artista_nome(artista_nome):
    return artista_schema.jsonify(Service_Artista.get_artista_by_nome(artista_nome))

@artista_blueprint.route("/artistas", methods=["POST"])
def create_artista():
    return artista_schema.jsonify(Service_Artista.add_artista(request.get_json()))


@artista_blueprint.route("/artistas/<int:artista_id", methods=["PUT"])
def update_artista(artista_id):
    return artista_schema.jsonify(Service_Artista.update_artista(artista_id, request.get_json()))


@artista_blueprint.route("/artistas/<int:artista_id", methods=["DELETE"])
def delete_artista(artista_id):
    return artista_schema.jsonify(Service_Artista.delete_artista(artista_id))
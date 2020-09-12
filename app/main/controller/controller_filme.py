from flask import Flask, jsonify, request, abort
from main.service import Service_Filme


@blueprint.errorhandler(404)
def not_found(error):
    print("error", error)
    return jsonify({"error": "Not found"}), 404


@blueprint.route("/filmes", methods=["GET"])
def get_filmes():
    return jsonify(Service_Filme.get_all_filmes)


#buscar pelo titulo
@blueprint.route("/filmes/<str:filme_titulo>", methods=["GET"])
def get_filme(filme_titulo):
    if Service_Filme.get_filme_by_titulo(filme_titulo) == None:
        abort(404)
    return jsonify(Service_Filme.get_filme_by_titulo)


@blueprint.route("/filmes", methods=["POST"])
def create_filme():
    Service_Filme.add_filme(dados)


@blueprint.route("/filmes/<int:filme_id>", methods=["PATCH"])
def update_filme(filme_id):
    Service_Filme.update_filme(filme_id)


@blueprint.route("/filmes/<int:filme_id>", methods=["DELETE"])
def delete_filme(filme_id):
    Service_Filme.delete_filme(filme_id)
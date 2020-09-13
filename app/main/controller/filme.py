from flask import request, jsonify, Blueprint
from ..service import Service_Filme
from ..model.Filme import filme_schema, filmes_schema

filme_blueprint = Blueprint('filmes', __name__)


@filme_blueprint.route('/filmes', methods=['GET'])
def get_filmes():
    return filmes_schema.jsonify(Service_Filme.get_all_filmes())


@filme_blueprint.route('/filmes/<filme_titulo>', methods=['GET'])
def get_filme(filme_titulo):
    return filme_schema.jsonify(Service_Filme.get_filme_by_titulo(filme_titulo))


@filme_blueprint.route('/filmes', methods=['POST'])
def create_filme():
    return filme_schema.jsonify(Service_Filme.add_filme(request.get_json()))


@filme_blueprint.route('/filmes/<int:filme_id>', methods=['PUT'])
def update_filme(filme_id):
    return filme_schema.jsonify(Service_Filme.update_filme(filme_id, request.get_json()))


@filme_blueprint.route('/filmes/<int:filme_id>', methods=['DELETE'])
def delete_filme(filme_id):
    return filme_schema.jsonify(Service_Filme.delete_filme(filme_id))

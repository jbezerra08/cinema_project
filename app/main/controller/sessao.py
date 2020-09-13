from flask import request, Blueprint
from ..service import Service_Sessao
from ..model.Sessao import sessao_schema, sessoes_schema

sessao_blueprint = Blueprint('sessoes', __name__)


@sessao_blueprint.route("/sessoes", methods=["GET"])
def get_sessoes():
    return sessoes_schema.jsonify(Service_Sessao.get_all_sessoes())


@sessao_blueprint.route("/sessoes/<int:sessao_id>", methods=["GET"])
def get_sessao(sessao_id):
    return sessao_schema.jsonify(Service_Sessao.get_sessao_by_id(sessao_id))


@sessao_blueprint.route("/sessoes", methods=["POST"])
def create_sessao():
    return sessao_schema.jsonify(Service_Sessao.add_sessao(request.get_json()))


@sessao_blueprint.route("/sessoes/<int:sessao_id>", methods=["PUT"])
def update_sessao(sessao_id):
    return sessao_schema.jsonify(Service_Sessao.update_sessao(sessao_id, request.get_json()))


@sessao_blueprint.route("/sessoes/<int:sessao_id>", methods=["DELETE"])
def delete_sessao(sessao_id):
    return sessao_schema.jsonify(Service_Sessao.delete_sessao(sessao_id))

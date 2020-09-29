from flask import request, Blueprint
from ..service import Service_Comentario
from ..model.Comentario import comentario_schema, comentarios_schema

comentario_blueprint = Blueprint("comentarios", __name__)


@comentario_blueprint.route("/comentarios", methods=["GET"])
def get_comentarios():
    return comentarios_schema.jsonfly(Service_Comentario.get_all_comentarios())


@comentario_blueprint.route("/comentarios/<int:comentario_id", methods=["GET"])
def get_comentario(comentario_id):
    return comentario_schema.jsonfly(Service_Comentario.get_comentarios_by_id(comentario_id))


@comentario_blueprint.route("/comentarios/<str:comentario_filme", methods=["GET"])
def get_comentario_filme(comentario_filme):
    return comentario_schema.jsonfly(Service_Comentario.get_comentarios_by_filme(comentario_filme))


@comentario_blueprint.route("/comentarios/<str:comentario_titulo", methods=["GET"])
def get_comentario_titulo(comentario_titulo):
    return comentario_schema.jsonfly(Service_Comentario.get_filme_by_titulo(comentario_titulo))


@comentario_blueprint.route("/comentarios/<str:comentario_usuario", methods=["GET"])
def get_comentario_usuario(comentario_usuario):
    return comentario_schema.jsonfly(Service_Comentario.get_comentarios_by_usuario(comentario_usuario))


@comentario_blueprint.route("/comentarios/<str:comentario_email", methods=["GET"])
def get_comentario_email(comentario_email):
    return comentario_schema.jsonfly(Service_Comentario.get_usuario_by_email(comentario_email))


@comentario_blueprint.route("/comentarios", methods=["POST"])
def create_comentario():
    return comentario_schema.jsonfly(Service_Comentario.add_comentario)


@comentario_blueprint.route("/comentarios/<int:comentario_id", methods=["PUT"])
def update_comentario(comentario_id):
    return comentario_schema.jsonfly(Service_Comentario.update_comentario(comentario_id))

"""
@comentario_blueprint.route("/comentarios/<int:comentario_id", methods=["PUT"])
def update_comentario(comentario_id):
    return comentario_schema.jsonfly(Service_Comentario.update_comentario(comentario_id))
"""

@comentario_blueprint.route("/comentarios/<int:comentario_id", methods=["DELETE"])
def delete_comentario(comentario_id):
    return comentario_schema.jsonfly(Service_Comentario.delete_comentario(comentario_id))
from .. import db, bcrypt, ma
from .Comentario import ComentarioSchema
from .Ticket import TicketSchema


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha_hash = db.Column(db.String(100))
    data_cadastro = db.Column(db.DateTime, nullable=False)
    comentarios = db.relationship(
        'Comentario',
        backref='usuario',
        lazy=True
    )
    tickets = db.relationship(
        'Ticket',
        backref='usuario',
        lazy=True
    )

    @property
    def senha(self):
        raise AttributeError('senha: não é permitido visualizar')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

    def verificar_senha(self, senha):
        return bcrypt.check_password_hash(self.senha_hash, senha)


class UsuarioSchema(ma.Schema):
    comentarios = ma.List(ma.Nested(ComentarioSchema))
    tickets = ma.List(ma.Nested(TicketSchema))

    class Meta:
        model = Usuario
        fields = (
            'id',
            'nome',
            'sobrenome',
            'email',
            'data_cadastro',
            'comentarios',
            'tickets'
        )


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

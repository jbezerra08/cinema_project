from .. import db, bcrypt


class Usuario(db.Model):
    """ Usuario Model para armazenar dados dos usuários """
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)  # 0 - 1
    nome = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha_hash = db.Column(db.String(100))
    registered_on = db.Column(db.DateTime, nullable=False)
    comentarios = db.relationship(
        'Comentario',
        backref='usuario',
        lazy=True
    )
    # entradas = db.relationship(
    #     'Entrada',
    #     backref='usuario',
    #     lazy=True
    # )

    @property
    def senha(self):
        raise AttributeError('senha: não é permitido visualizar')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

    def check_senha(self, senha):
        return bcrypt.check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f'Id: {self.public_id} Usuário: {self.nome}'

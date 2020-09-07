from .. import db, bcrypt


class Usuario(db.Model):
    """ Usuario Model para armazenar dados dos usuários """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    nome = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha_hash = db.Column(db.String(100))
    registered_on = db.Column(db.DateTime, nullable=False)

    @property
    def password(self):
        raise AttributeError('senha: não é permitido visualizar')

    @password.setter
    def password(self, senha):
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

    def check_password(self, senha):
        return bcrypt.check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f'Id: {self.public_id} Usuário: {self.nome}'

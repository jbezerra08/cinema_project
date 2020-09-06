
class Usuario():
    
    def __init__(self, id, nome, email, cpf):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.administrador = False
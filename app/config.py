# False para produção
# True para desenvolvimento
DEBUG = True

# ip = localhost, caso o acesso ao bd seja local
uri_db = 'mysql+pymysql://usuario:senha@ip/nome-do-db'

SQLALCHEMY_DATABASE_URI = uri_db

SQLALCHEMY_TRACK_MODIFICATIONS = False

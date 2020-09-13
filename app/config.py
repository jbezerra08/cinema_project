# False para produção
# True para desenvolvimento
DEBUG = True

# caso o acesso ao bd seja local
# ip = "localhost"
# uri_db = 'mysql+pymysql://usuario:senha@ip/db_nome'
uri_db = 'sqlite:///db_cinema.db'  # /app/main/db_cinema.db

SQLALCHEMY_DATABASE_URI = uri_db

SQLALCHEMY_TRACK_MODIFICATIONS = False

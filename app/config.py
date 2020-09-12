# False para produção
# True para desenvolvimento
DEBUG = True

ip = "localhost" # caso o acesso ao bd seja local
uri_db = 'mysql+pymysql://jb:96033023@'+ip+'/test'
#uri_db = 'sqlite:///db_cinema.db'  # /app/main/db_cinema.db

SQLALCHEMY_DATABASE_URI = uri_db

SQLALCHEMY_TRACK_MODIFICATIONS = False

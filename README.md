# cinema_project
Aplicação back-end para catologar e gerenciar filmes.

## Tecnologias utilizadas

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)

## Configurando Virtual environment

- [Pipenv](https://docs.pipenv.org/en/latest/)

        - pipenv --three
        - pipenv shell
        - pipenv install -r requirements.txt

- [Virtualenv](https://docs.python.org/3/library/venv.html)

        - python3 -m venv env
        - source env/bin/activate
        - pip install -r requirements.txt

## Configurando ambiente de desenvolvimento

    Teste

        - app/create_db.py -> app = create_app('config.ConfigTest')
        - app/run.py -> app = create_app('config.ConfigTest')
    
    Desenvolvimento

        - app/create_db.py -> app = create_app('config.ConfigDesenvolvimento')
        - app/run.py -> app = create_app('config.ConfigDesenvolvimento')
    
    Produção

        - app/create_db.py -> app = create_app('config.ProdConfig')
        - app/run.py -> app = create_app('config.ProdConfig')

## Executando a aplicação

    Salvando dados para teste

        - python app/create_db.py
    
    Iniciando aplicação Flask

        - python app/run.py


## Documentação

- [Postman Doc](https://documenter.getpostman.com/view/9922970/TVRdArxw)

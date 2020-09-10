from main import create_app, db
from datetime import date, datetime
from json import dumps

from main.service.Service_Usuario import add_usuario
from main.service.Service_Filme import add_filme, delete_filme, get_filme_by_id
from main.service.Service_Genero import add_genero
from main.service.Service_Artista import add_artista
from main.service.Service_Sala import add_sala
from main.service.Service_Comentario import add_comentario
from main.service.Service_Sessao import add_sessao

from main.model.Filme import Filme

app = create_app('config')

usuarios = [
    {
        'nome': 'matheus',
        'email': 'matheus@email.com',
        'senha': '123456'
    },
    {
        'nome': 'jailson',
        'email': 'jailson@email.com',
        'senha': '654321'
    }
]

generos = [
    {'tipo': 'Aventura'},
    {'tipo': 'Horror'},
    {'tipo': 'Comédia'},
    {'tipo': 'Romance'}
]

atores = [
    {'nome': 'Ed Jhonson'},
    {'nome': 'Tom anderson'},
    {'nome': 'Roberta Julie'},
    {'nome': 'Oliver Twist'},
]

filmes = [
    {
        'titulo': 'titulo1',
        'lancamento': '2020/05/15',
        'duracao': '145 minutos',
        'sinopse': 'sinopse qualquer',
        'enredo': 'enredo qualquer',
        'generos': ['Aventura', 'Comédia'],
        'elenco': ['Ed Jhonson', 'Oliver Twist', 'Roberta Julie']
    },
    {
        'titulo': 'titulo2',
        'lancamento': '2008/02/23',
        'duracao': '90 minutos',
        'sinopse': 'sinopse qualquer',
        'enredo': 'enredo qualquer',
        'generos': ['Horror'],
        'elenco': ['Ed Jhonson', 'Roberta Julie', 'Tom anderson']
    }
]

salas = [
    {
        'numero': 23,
        'total_assentos': 87
    },
    {
        'numero': 22,
        'total_assentos': 75
    },
    {
        'numero': 21,
        'total_assentos': 120
    }
]

sessoes = [
    {
        'titulo': 'titulo1',
        'numero': 22,
        'data': '2020/11/09',
        'horario': '20:00',
    },
    {
        'titulo': 'titulo2',
        'numero': 23,
        'data': '2020/12/22',
        'horario': '19:30',
    },
    {
        'titulo': 'titulo2',  # não cadastra mesmo sala/horário/dia
        'numero': 22,
        'data': '2020/11/09',
        'horario': '20:00',
    }
]

comentarios = [
    {
        'titulo': 'titulo2',
        'nome': 'matheus',
        'texto_comentario': 'Filme não assusta muito.'
    },
    {
        'titulo': 'titulo2',
        'nome': 'jailson',
        'texto_comentario': 'Legal.'
    }
]

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('[+] Database created')
        [add_usuario(usuario) for usuario in usuarios]
        print('[+] Usuarios created')
        [add_artista(ator) for ator in atores]
        print('[+] Artistas created')
        [add_genero(genero) for genero in generos]
        print('[+] Generos created')
        [add_filme(filme) for filme in filmes]
        print('[+] Filmes created')
        [add_sala(sala) for sala in salas]
        print('[+] Salas created')
        [add_comentario(comentario) for comentario in comentarios]
        print('[+] Comentarios created')
        [add_sessao(sessao) for sessao in sessoes]
        print('[+] Sessoes created')

        teste1 = get_filme_by_id({'id': 2})
        print(teste1)

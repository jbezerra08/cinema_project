from main import create_app, db

from main.service import Service_Usuario
from main.service import Service_Filme
from main.service import Service_Genero
from main.service import Service_Artista
from main.service import Service_Sala
from main.service import Service_Comentario
from main.service import Service_Sessao
from main.service import Service_Ticket

app = create_app('config')

usuarios = [
    {
        'nome': 'matheus',
        'sobrenome': 'matias',
        'email': 'matheus@email.com',
        'senha': '123456'
    },
    {
        'nome': 'francisco',
        'sobrenome': 'jailson',
        'email': 'jailson@email.com',
        'senha': '654321'
    },
    {
        'nome': 'matheus',
        'sobrenome': 'matias',
        'email': 'matheus@email.com',
        'senha': '123456'
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
        'preco': 12.40
    },
    {
        'titulo': 'titulo2',
        'numero': 23,
        'data': '2020/12/22',
        'horario': '19:30',
        'preco': 15.00
    },
    {
        'titulo': 'titulo2',  # não cadastra mesmo sala/horário/dia
        'numero': 22,
        'data': '2020/11/09',
        'horario': '20:00',
        'preco': 16.00
    }
]

tickets = [
    {
        'id': 2,
        'email': 'matheus@email.com',
        'quantidade_comprada': 1
    },
    {
        'id': 2,
        'email': 'jailson@email.com',
        'quantidade_comprada': 1
    }
]

comentarios = [
    {
        'titulo': 'titulo2',
        'email': 'matheus@email.com',
        'texto_comentario': 'Filme não assusta muito.'
    },
    {
        'titulo': 'titulo2',
        'email': 'jailson@email.com',
        'texto_comentario': 'Legal.'
    }
]

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('[+] Database created')
        [Service_Usuario.add_usuario(usuario) for usuario in usuarios]
        print('[+] Usuarios created')
        [Service_Artista.add_artista(ator) for ator in atores]
        print('[+] Artistas created')
        [Service_Genero.add_genero(genero) for genero in generos]
        print('[+] Generos created')
        [Service_Filme.add_filme(filme) for filme in filmes]
        print('[+] Filmes created')
        [Service_Sala.add_sala(sala) for sala in salas]
        print('[+] Salas created')
        [Service_Comentario.add_comentario(comentario) for comentario in comentarios]
        print('[+] Comentarios created')
        [Service_Sessao.add_sessao(sessao) for sessao in sessoes]
        print('[+] Sessoes created')
        [Service_Ticket.add_ticket(ticket) for ticket in tickets]
        print('[+] Tickets created')

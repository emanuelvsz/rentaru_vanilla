import datetime
import time
import csv
import os

from queries import *
from helpers import *
from models import Rent
from collectors.menu_options import *


def listar_filmes():
    os.system('clear')
    while not input_ready():
        os.system('clear')
        print("---------------- Catálogo ----------------\n")
        data = get_movies()
        for movie in data:
            display_movie_details(movie)
        print("-------- Pressione qualquer tecla --------")
        escolha = input()
        break
    os.system('clear')
    
def listar_filme_por_id():
    os.system('clear')
    movie_id = input("Digite o ID do filme: ")
    while not input_ready():
        os.system('clear')
        data = get_movie_by_id(movie_id)
        if data:
            movie_dict = {
                'id': data[0],
                'title': data[1],
                'price': data[2],
                'avaiable': data[3]
            }
            print("-------------- Dados de", movie_dict['title'], "--------------\n")
            print("ID:           ", movie_dict['id'])
            print("Título:       ", movie_dict['title'])
            print("Preço:        ", movie_dict['price'], "R$")
            print("Disponível:   ", movie_dict['avaiable'])
        else:
            print("Filme não encontrado.")
        print("\n----------- Pressione qualquer tecla -----------")
        escolha = input()
        break
    os.system('clear')
    
def alugar_filme():
    os.system('clear')
    filme_id = input("Digite o ID do filme que quer alugar: ")
    data = get_movie_by_id(filme_id)
    if not data:
        print("Filme inválido: O filme digitado não existe")
        return
    movie_dict = {
        'id': data[0],
        'title': data[1],
        'price': data[2],
        'avaiable': data[3]
    }
    if movie_dict['avaiable'] == 'false':
        print("\nEsse filme não está disponível!")
        time.sleep(2)
        return
    user_id = input("Digite o ID do usuário que quer alugar: ")
    new_rent = Rent()
    new_rent.user_id = user_id
    new_rent.movie_id = movie_dict['id']
    new_rent.rented_at = datetime.date.today()
    insert_into_rent(new_rent)
    update_availability(new_rent.movie_id, False)
    time.sleep(3)
    
def devolver_filme():
    os.system('clear')
    filme_id = input("Digite o ID do filme que quer devolver: ")
    data = get_movie_by_id(filme_id)
    if not data:
        os.system('clear')
        print("Filme inválido: O filme digitado não existe")
        time.sleep(2)
        return
    movie_dict = {
        'id': data[0],
        'title': data[1],
        'price': data[2],
        'avaiable': data[3]
    }
    if movie_dict['avaiable'] == "true":
        print("Filme inválido: O filme não está alugado! Você pode aluga-lo")
        time.sleep(2)
        return
    update_availability(movie_dict['id'], True)
    
def listar_filmes_por_usuario():
    os.system('clear')
    user_id = input("Digite o ID do usuário para listar os filmes alugados: ")
    rented_movies = buscar_filmes_alugados_por_usuario(user_id)
    os.system('clear')
    print("---------------- Filmes Alugados por Usuário ----------------\n")
    if rented_movies:
        for movie in rented_movies:
            print("ID:       ", movie['id'])
            print("Título:   ", movie['title'])
            print("Preço:    ", movie['price'], "R$")
            print("Alugado em:", movie['rented_at'], "\n")
    else:
        print("Nenhum filme alugado por este usuário.\n")
    print("-------- Pressione qualquer tecla para voltar --------")
    escolha = input()
    os.system('clear')
    user_menu()

def adicionar_filme():
    os.system('clear')
    filme_path = 'db/movie.csv'
    titulo = input("Digite o título do filme: ")
    preco = input("Digite o preço do filme: ")
    avaiable = True
    with open(filme_path, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        linhas = list(leitor_csv)
    if len(linhas) > 0:
        ultimo_id = int(linhas[-1][0])
        novo_id = ultimo_id + 1
    else:
        novo_id = 1
    with open(filme_path, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        escritor_csv.writerow([novo_id, titulo, preco, avaiable])
        
def adicionar_usuario():
    os.system('clear')
    filme_path = 'db/user.csv'
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    
    avaiable = True
    with open(filme_path, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        linhas = list(leitor_csv)
    if len(linhas) > 0:
        ultimo_id = int(linhas[-1][0])
        novo_id = ultimo_id + 1
    else:
        novo_id = 1
    with open(filme_path, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        escritor_csv.writerow([novo_id, email, nome, senha, "user"])

def display_movie_details(data):
    if len(data) >= 4:
        movie_dict = {
            'id': data[0],
            'title': data[1],
            'price': data[2],
            'avaiable': data[3]
        }
        print("ID:           ", movie_dict['id'])
        print("Título:       ", movie_dict['title'])
        print("Preço:        ", movie_dict['price'], "R$")
        print("Disponível:   ", movie_dict['avaiable'], "\n")
    else:
        print("")

import time
import csv
import os

from helpers import input_ready, print_blinking_rainbow_menu
from queries import get_movies


def movie_catalog():
    os.system('clear')
    while not input_ready():
        os.system('clear')
        print("---------------- Catálogo ----------------\n")
        print("             ID  NOME  PREÇO              \n")
        data = get_movies()
        for movie in data:
            print(movie)
        print("-------- Pressione qualquer tecla --------")
        escolha = input()
        break
    os.system('clear')

def adicionar_filme():
    os.system('clear')
    caminho_do_arquivo = 'db/movie.csv'
    titulo = input("Digite o título do filme: ")
    preco = input("Digite o preço do filme: ")
    with open(caminho_do_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        linhas = list(leitor_csv)
    if len(linhas) > 0:
        ultimo_id = int(linhas[-1][0])
        novo_id = ultimo_id + 1
    else:
        novo_id = 1
    with open(caminho_do_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        escritor_csv.writerow([novo_id, titulo, preco])


import time
import csv
import os

from helpers import input_ready
from queries import get_movies

def print_colorful_line(line, color):
    return "\033[{}m{}\033[0m".format(color, line)

def movie_catalog():
    os.system('clear')
    cores = ["91", "92", "94", "95", "96", "97"]

    while not input_ready():
        for cor in cores:
            os.system('clear')
            print("\033[{}m--------------------------- Catálogo de Filmes ---------------------------\033[0m".format(cor))
            get_movies()
            print(print_colorful_line("--------------", cor), " Pressione 'a' para adicionar um filme, ou qualquer outra tecla para continuar... ", print_colorful_line("--------------", cor))
            time.sleep(0.3)

        escolha = input("Escolha uma opção: ")
        if escolha.lower() == 'a':
            adicionar_filme()

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


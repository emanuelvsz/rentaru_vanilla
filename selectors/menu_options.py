import os

from helpers import *

def login():
    print("Login realizado com sucesso!")
        
def sair():
    os.system('clear')
    print("Saindo do terminal. Até logo!")
    exit()

def print_main_menu():
    os.system('clear')
    print("-------------- Menu Principal --------------\n")
    print("1. Catálogo de Filmes")
    print("2. Dados de um Filme")
    print("3. Alugar um Filme")
    print("4. Devolver um Filme")
    print("5. Meus Filmes")
    print("0. Sair\n")
    print("-- Selecione alguma opção para prosseguir --")
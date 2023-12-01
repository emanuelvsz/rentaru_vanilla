import time
import os

from selectors.movie_selectors import *
from selectors.menu_options import *
from helpers import *


def login():
    print("Login realizado com sucesso!")
        
def sair():
    os.system('clear')
    print("Saindo do terminal. Até logo!")
    exit()

def user_menu():
    os.system('clear')
    print("-------------- Menu de Usuário --------------\n")
    print("1. Catálogo de Filmes")
    print("2. Dados de um Filme")
    print("3. Alugar um Filme")
    print("4. Devolver um Filme")
    print("5. Meus Filmes")
    print("0. Sair\n")
    print("--- Selecione alguma opção para prosseguir ---")
    escolha = input()
    if escolha == "1":
        listar_filmes()
    elif escolha == "2":
        listar_filme_por_id()
    elif escolha == "3":
        alugar_filme()
    elif escolha == "4":
        devolver_filme()
    elif escolha == "5":
        listar_filmes_por_usuario()
    elif escolha == "0":
        sair()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
        
def admin_menu():
    os.system('clear')
    print("-------------- Menu de Admin --------------\n")
    print("1. Catálogo de Filmes")
    print("2. Adicionar Filme")
    print("3. Adicionar Usuário")
    print("0. Sair\n")
    print("-- Selecione alguma opção para prosseguir --")
    escolha = input()
    if escolha == "1":
        listar_filmes()
    elif escolha == "2":
        adicionar_filme()
    elif escolha == "0":
        sair()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
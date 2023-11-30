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
    print("-------------- Menu principal --------------\n")
    print("1. Login")
    print("2. Catálogo de Filmes")
    print("3. Sair\n")
    print("-- Selecione alguma opção para prosseguir --")
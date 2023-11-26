import time
import sys
import os

from queries.get_all import get_data

def login():
    os.system('clear')
    print("Você fez login com sucesso!")
    time.sleep(2)
    os.system('clear')
    
        
def sair():
    os.system('clear')
    print("Saindo do terminal. Até logo!")
    exit()

def exibir_menu():
    os.system('clear')
    print("\n===== Menu =====")
    print("1. Login")
    print("2. Catálogo de Filmes")
    print("3. Sair")
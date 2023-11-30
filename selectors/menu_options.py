import os

def login():
    print("Login realizado com sucesso!")
        
def sair():
    os.system('clear')
    print("Saindo do terminal. Até logo!")
    exit()

def main_menu():
    os.system('clear')
    print("\n===== Menu =====")
    print("1. Login")
    print("2. Catálogo de Filmes")
    print("3. Sair")
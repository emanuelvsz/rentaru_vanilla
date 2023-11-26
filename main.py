from selectors.menu_options import *
from selectors.movie_catalog import *

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            login()
        elif escolha == "2":
            catalogo_filmes()
        elif escolha == "3":
            sair()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

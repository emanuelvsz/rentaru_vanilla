import time

from selectors.menu_options import *
from selectors.movie_selectors import *


def main():
    while True:
        print_main_menu()
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

if __name__ == "__main__":
    main()

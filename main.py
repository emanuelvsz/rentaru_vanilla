from selectors.menu_options import *
from selectors.movie_catalog import *

import time

def main():
    while True:
        print_main_menu()
        escolha = input()
        if escolha == "1":
            login()
        elif escolha == "2":
            movie_catalog()
        elif escolha == "3":
            sair()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    main()

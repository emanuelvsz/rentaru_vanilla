import time
import sys
import os

from queries.get_all import get_data

def print_colorful_line(line, color):
    return "\033[{}m{}\033[0m".format(color, line)

def catalogo_filmes():
    os.system('clear')
    caminho_do_arquivo = 'db/movie.csv'
    cores = ["91", "92", "94", "95", "96", "97"]
    while not input_ready():
        for cor in cores:
            os.system('clear')
            print("\033[{}m--------------------------- Catálogo de Filmes ---------------------------\033[0m".format(cor))
            get_data(caminho_do_arquivo)
            print(print_colorful_line("--------------", cor), " Pressione qualquer tecla para continuar... ", print_colorful_line("--------------", cor))
            time.sleep(0.3)
    os.system('clear')

def input_ready():
    try:
        if os.name == 'nt':
            return
        else:
            import select
            return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    except:
        return False
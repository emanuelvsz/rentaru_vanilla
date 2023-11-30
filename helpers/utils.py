import time
import sys
import os 

from colorama import Fore, Style

def print_blinking_rainbow_menu(header_text, bottom_text, data):
    line = "--------------"
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    blink_frequency = 0.5

    # Imprime o cabeçalho sem piscar
    print(f"{Fore.RED}{line} {header_text} {Style.RESET_ALL}")

    # Piscar todas as linhas ao redor dos dados
    for color in colors:
        print(f"{color}{line} {Style.RESET_ALL}")

    # Exibe os dados entre as linhas do cabeçalho e do rodapé
    for item in data:
        for color in colors:
            print(f"{color}{item}{Style.RESET_ALL}")
            time.sleep(blink_frequency)

    # Piscar todas as linhas novamente
    for color in colors:
        print(f"{color} {line}{Style.RESET_ALL}")
        time.sleep(blink_frequency)

    # Imprime o rodapé sem piscar
    print(f"{Fore.CYAN}{line} {bottom_text} {Style.RESET_ALL}")

def input_ready():
    try:
        if os.name == 'nt':
            return
        else:
            import select
            return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    except:
        return False
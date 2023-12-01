from selectors.menu_options import user_menu, admin_menu

def main():
    while True:
        print("Selecione uma opção:")
        print("1. Login como usuário")
        print("2. Login como administrador")
        print("3. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == "1":
            user_menu()
        elif escolha == "2":
            admin_menu()
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

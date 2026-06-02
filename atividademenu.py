def exibe_menu():
    print("\n===== MENU =====")
    print("1 - Bem vindo!")
    print("2 - Sobre o curso")
    print("3 - Ajuda (sobre o exercício). ")
    print("0 - Sair")
    print("=================")

def saudacao():
    nome = input("Digite seu nome: ")
    print(f"Bem vindo ao curso, {nome}! ")

def sobre():
    print("O curso Jovem programador tem como objetivo ensinar os jovens a programar.")

def ajuda():
    print("Está utilizando o loop infinito, utilizando o While")

while True:
    exibe_menu()
    menu = input(" Digite a opção desejada! ")
    if menu == "0": break
    elif menu == "1": saudacao()
    elif menu == "2": sobre()
    elif menu == "3": ajuda()
    else: print("Opção inválida! Tente novamente!")
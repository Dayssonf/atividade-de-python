def somar(n1, n2):
    total = n1 + n2
    print(f" A soma é: {total}")

def subtrair(n1, n2):
    total = n1 - n2
    print(f"A subtração é: {total}")

def multiplicar(n1, n2):
    total = n1 * n2
    print(f"A Multiplicação é: {total}")

def dividir(n1, n2):
    total = n1 / n2
    print(f"A divisão é: {total}")



while True:
    print("\n==== CALCULADORA===")

    print("1 soma (+)")
    print("2 Subtração (-)")
    print("3 Multiplicação (*)")
    print("4 Divisão (/)")
    print("5 Sair")

    menu = input("Digite a Opção: ")
    if menu == "5":
        print("Encerrando o programa... ")
        break
    if menu not in ["1", "2", "3", "4", "5"]:
        print("Opção Inválida! Tente novamente")
        continue

    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite um número: "))

    if menu == "1": somar(n1, n2)
    
    elif menu == "2": subtrair(n1, n2)
    
    elif menu == "3": multiplicar(n1, n2)

    elif menu == "4": dividir(n1,n2)
    
    else:
        print("Encerrando...")
        break
        

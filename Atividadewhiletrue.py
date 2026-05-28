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
    n1 = float(input("Digite um números: "))
    n2 = float(input(" DIgite um número: "))

    if menu == "1":
        print(f" A soma é: {n1 + n2}")
    
    elif menu == "2":
        print(f"A subtração é: {n1 - n2}")
    
    elif menu == "3":
        print(f"A Multiplicação é: {n1 * n2}")

    elif menu == "4":
        print(f"A divisão é: {n1 / n2}")
    
    else:
        print("Encerrando...")
        break
        

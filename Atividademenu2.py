def exibir_mmenu():
    print(" ==============")
    print("Menu: ")
    print("1 - Depositar. ")
    print("2 - sacar. ")
    print("3 - Ver saldo. ")
    print("0 - Sair. ")
    print("==============")

def depositar(saldo):
    valor = float(input("Digite um valor para depósito: "))
    saldo = saldo + valor
    print(f"Depósito de R${valor} realizado!")
    return saldo

def sacar(saldo):
    saque = float(input("Digite um valor para saque: "))
    if saque > saldo:
        print("Saldo insuficiente!")
        return saldo
    saldo = saldo - saque
    print(f"Depósito de {saque} realizado!")
    return saldo

def ver_saldo(saldo):
    print(f"O saldo atual: {saldo}")

  
saldo = 0.0
while True:
    exibir_mmenu()
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        print("Encerrando o programa...")
        break
    elif opcao == "1":
        saldo = depositar(saldo)
    elif opcao == "2":
        saldo = sacar(saldo)
    elif opcao == "3":
        ver_saldo(saldo)
    else:
        print("Opção inválida. ")
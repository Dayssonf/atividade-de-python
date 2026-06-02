def conversor():
    print("====== MENU ======")
    print("1 - Converta Celsius para Fahrenheit")
    print("2 - Converta Reais para dólar")
    print("3 - Converta horas para minutos")
    print("0 - Encerrando o programa...")
    print("==================")

def temperatura():
    celcius = float(input("Digite a temperatura: "))
    fh = celcius * 1.8 + 32
    print(f"Fahrenheit: {fh}")

def dinheiro():
    reais = float(input(" Digite um valor: "))
    dolar = reais / 5.04
    print(f"Dólares: ${dolar}")

def relogio():
    horas = float(input(" Digite as horas: "))
    minutos = horas * 60
    print(f"minutos: {minutos} ")

while True:
    conversor()
    opcao = input("DIgite a opção desejada: ")
    if opcao == "0": break
    elif opcao == "1": temperatura()
    elif opcao == "2": dinheiro()
    elif opcao == "3": relogio()
    else: print("Inválido...")
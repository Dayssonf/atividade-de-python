velocidade = int(input("Digite a velocidade do carro: "))

if velocidade >=1 and velocidade <= 60:
    print("Dentro do limite de velocidade ")
elif velocidade >=61 and velocidade <=80:
    print("Dentro do limite de velocidade ")
elif velocidade == 0:
    print("Carro parado! ")
elif velocidade < 0:
    print("Velocidade inválida! ")
else:
    print("Multa grave!")
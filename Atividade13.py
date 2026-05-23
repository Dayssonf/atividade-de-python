nomes = ["Daysson", "Juliano","Pedro", "João"]
notas = [10, 9, 3, 6]
frequencias = [100, 95, 75, 55]

for posicao, nome in enumerate(nomes):

    if notas[posicao] >=7 and frequencias[posicao] >=75:
        print(f"{nome}, Aprovado!")
    else: 
        print(f"{nome}, Reprovado!")


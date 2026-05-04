n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3) / 3
media = round(media, 2)

print("A média foi: ", media)

if media >=1 and media <=3:
    print("Reprovado")

elif media >=4 and media <=6:
    print("Em recuperação")

else:
    print("Aprovado")
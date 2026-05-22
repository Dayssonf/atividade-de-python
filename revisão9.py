produtos = ["Arroz", "Feijão", "Ovos"]
precos = [5.99, 6.99, 12.99]

for posicao, produto in enumerate(produtos):
    if precos[posicao] < 10:
        preco_ajustado = round(precos[posicao] * 1.10, 2) #arredondamento decimal. No final as casas(2)
        print(f"O produto:{produto} passa a custar R${preco_ajustado}")
    else:
            print(f"O {produto}, custa R${precos[posicao]}")


produto = ["trigo", "acucar", "arroz", "feijao", "macarrao"]
precos =  [19.98, 20.00, 23.30, 12.00, 6.99]
quantidades = [2, 2, 4, 4, 3]
subtotais = []

# Antes, faria assim para pegar o produto e preço:


for indice, produto in enumerate (produto):
    preco = precos[indice] #preco = precos[0]
    quantidade = quantidades[indice]
    subtotal = quantidade * preco
    subtotais.append(subtotal)

    mensagem = f"""
    ---------------------------------
    produto: {produto}
    quantidade: {quantidade}
    Valor unitário: {preco}
    Subtotal: {subtotal}
    --------------------------
    """

    print(mensagem)

print(subtotais)

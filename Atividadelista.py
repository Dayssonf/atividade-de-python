mercado = ["trigo", "acucar", "arroz", "feijao", "macarrao"]
preco =  [19.98, 20.00, 23.30, 12.00, 6.99]
print(mercado)
print(mercado[0]) # imprime "trigo"
print(mercado[-1]) # imprime "acucar"
print(len(mercado))

#exiba o nome e o preço dele
print(f"o {mercado[0]} custa R${preco[0]}.")

#remova o último produto
mercado.remove(mercado[-1])
preco.remove(preco[-1])

#Para somar o preço de todos os produtos

total = sum(preco)
print(f"O total deu R${total}")

#lógica condicional if/else para desconto:

if total < 100:
    exit()
else:
    desconto = 0.95
    total = total * desconto
    print(f"O total agora com deconto é de R$ {total}.")
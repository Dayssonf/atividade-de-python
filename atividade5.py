valor = float (input("Digite o valor do pedido: "))
if valor >= 100:
    total = valor * 0.90
    print("valor total foi de:", total)
else:
   total = valor
   print("valor total foi de:", total)
   
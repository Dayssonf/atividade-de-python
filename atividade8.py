valor = float (input("Digite o valor do pedido: "))
""" 
Regra de Negócio:
*Se a venda for até 100 reais, dê 5% de deconto
*Se a venda for entre 101.01 e 299.99 reais, dê 10% de desconto
*Se a venda for acima de 300 reais, dê 15% de deconto

"""

if   valor <= 100:
    desconto = 0.95

elif valor > 100 and valor <= 299.99:
    desconto = 0.90

else:
   desconto = 0.85
   

total = valor * desconto
descontopercentual = (1- desconto) * 100
descontopercentual = int(descontopercentual)
print("Valor total foi de:", total, "Seu desconto foi de:", descontopercentual)   

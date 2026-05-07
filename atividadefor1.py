frutas = ["maça","banana", "manga", "ameixa", "carambola"]

frutas_favorita = input("Qual sua fruta favorita: ")

#Caso a fruta favorita NÂO ESTÀ na lista frutas
if frutas_favorita not in frutas:
    #faça isso: (Exibir mensagem e sai do sistema):
    print("Sua fruta favorita não está na lista! ")
    exit()

# Para cada posição (Indice) e fruta na lista numerada de frutas
for posicao, fruta in enumerate(frutas):
     # faça isso:
     # SE a fruta dessa iteração é igual a fruta favorita
    if fruta == frutas_favorita:
        # Salva numa nova variável a posição dessa iteração
        posicao_fruta_favorita = posicao
        # QUebra o for (faz ele parar)
        break

# Saída do algoritmo (Print)
print(f"Minha fruta favorita está na posição índica{posicao_fruta_favorita} ")
produtos = ("Óleo", "Lanterna", "Filtro", "Carburador")
preco_produtos = (380, 95, 110, 890)

servicos = ("Lavação", "Troca de Óleo", "Troca de Filtro", "Limpeza do carburador")
preco_servicos = (100, 310, 120, 290)

while True:

    print("1 - Ver Produtos")
    print("2 - Ver Serviços")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao ==1:
        for i, produto in  enumerate(produtos):
            print(i, "-", produto, "- R$", preco_produtos[i])

        escolha = int(input("\n Digite o número do produto: "))

        nome_item = produtos[escolha]

        valor_original = preco_produtos[escolha]

        if valor_original >300:
            valor_final = valor_original * 0.90

        else:
            valor_final = valor_original

        print("item:", nome_item)
        
        print("Valor final: R$", valor_final)

    elif opcao ==2:
        for i, servico in enumerate(servicos):
            print(i, "-", servico, "- R$", preco_servicos[i])

        escolha = int(input("\n Digite o número do serviço: "))

        nome_item = servicos[escolha]

        if valor_original >300:
            valor_final = valor_original *0.90
        
        else:
            valor_final = valor_original

        print("Serviço: ", nome_item)
        print("Valor final: R$", valor_final)

    elif opcao == 3:
        print("Encerrando o atendimento... ")
        break
    
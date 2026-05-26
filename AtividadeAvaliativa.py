produtos = ("Oleo", "Filtro", "Lanterna", "Mola")

preco_produto = (300, 50, 60, 95)

servicos = ("Lavacao", "Troca de oleo", "Troca de pneu", "Balanceamento")

preco_servico = (100, 300, 450, 180)

while True:
    print("1 - Ver produtos")
    print("2 - Ver servicos")
    print("3 - Sair")

    opcao = int(input("Escolha uma opcao: "))

    # PRODUTOS

    if opcao == 1:

        for i, produto in enumerate(produtos):

            print(i, "-", produto, "- R$", preco_produto[i])

        escolha = int(input("\nDigite o numero do produto: "))

        nome_item = produtos[escolha]

        valor_original = preco_produto[escolha]

        # DESCONTO

        if valor_original > 300:

            valor_final = valor_original * 0.90

        else:

            valor_final = valor_original

        # CUPOM

        print("Item:", nome_item)

        print("Valor final: R$", valor_final)

    # SERVICOS

    elif opcao == 2:


        for i, servico in enumerate(servicos):

            print(i, "-", servico, "- R$", preco_servico[i])

        escolha = int(input("\nDigite o numero do servico: "))

        nome_item = servicos[escolha]

        valor_original = preco_servico[escolha]

        # DESCONTO

        if valor_original > 300:

            valor_final = valor_original * 0.90

        else:

            valor_final = valor_original

        # CUPOM

        print("Servico:", nome_item)

        print("Valor final: R$", valor_final)

    # SAIR

    elif opcao == 3:

        print("Encerrando sistema...")

        break

    else:

        print("Opcao invalida!")
 
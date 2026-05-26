produtos = ("Oleo", "Filtro", "Lanterna", "Mola")
preco_produto = (300, 50, 60, 95)
servicos = ("lavacao", "troca de oleo", "troca de pneu", "balanceamento")
preco_servico = (100, 300, 450, 180)

while True:

    print("1 - ver produtos")
    print("2 -ver serviços")
    print("3 -Sair")
    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        print("produtos: ")
        for i, produto in enumerate(produtos):
            print(produtos[i], "R$ ", preco_produto[i])
    elif opcao == 2:
        print("servicos: ")
        for i, servico in enumerate(servicos):
            escolha = int(input("Digite o número do item: "))
            print(servicos[i], "R$ ", preco_servico[i])
    elif opcao == 3:
        print("Encerrando...")
        break
    else:
        print("Opção inválida")
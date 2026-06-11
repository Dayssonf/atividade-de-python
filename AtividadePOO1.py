class Produto:
    def __init__(self, nome, preco, qnt=0):

        self.nome = nome
        self.preco = preco
        self.qnt = qnt
    
    def exibir(self):
        print(f"Produto {self.nome}: | Preço R${self.preco} | Quantidade: {self.qnt}")

def exibir_menu():
    print("==========")
    print("1- Cadastrar produto")
    print("2= Exibir produtos ")
    print("0 - Sair!")
    print("==========")

def cadastrar_produto():
    print("\n CADASTRANDO PRODUTO... ")
    nome = input("Digite o nome do Produto: ")
    preco = float(input("Digite o preço do produto: "))
    qnt = int(input("Digite a quantidade do produto: "))
    produto = Produto(nome, preco, qnt)
    produtos.append(produto)

def exibe_produtos():
    if not produtos:
        print("Não há produtos cadastrados!")
        return

    for produto in produtos:
        produto.exibir()
        


produtos = []
while True:
    exibir_menu()
    opcao = input("Escolha a opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        exibe_produtos()
    else:
        print("Opção inválida...")    

        
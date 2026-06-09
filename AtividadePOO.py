class Produto:
    def __init__(self, nome, preco, qnt):

        self.nome = nome
        self.preco = preco
        self.qnt = qnt
    
    def exibir(self):
        print(f"Produto {self.nome}: | Preço R${self.preco} | Quantidade: {self.qnt}")

produto_1 = Produto("Feijão", 20.0, 2)
produto_2 = Produto("Arroz", 8.50, 20)

produto_1.exibir()
produto_2.exibir()
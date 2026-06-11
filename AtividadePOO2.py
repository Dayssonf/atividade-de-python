class Alunos:
    def __init__(self, nome, idade, nota):

        self.nome = nome
        self.idade = idade
        self.nota = nota

    def exibir(self):
        print(f"Aluno: {self.nome} | Idade {self.idade} | Nota {self.nota}")
    
    def situacao(self):
        if self.nota <=6:
            print("Reprovado")
        elif self.nota <=10 and self.nota >=7:
            print("Aprovado")
        else:
            print("Número inválido...")

def cadastrar_aluno():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    nota = float(input("Digite a sua nota: "))
    aluno = Alunos(nome, idade, nota)
    aluno.exibir()
    aluno.situacao()


while True:
    cadastrar_aluno()
    break
    
    


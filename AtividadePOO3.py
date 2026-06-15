class Alunos:
    def __init__(self, nome, notas):

        self.nome = nome
        self.notas = notas

    def exibir(self):
        print(f"Aluno: {self.nome}")
        if self.notas:
            for ordem_nota, nota in enumerate(self.notas, 1):
                print(f"Nota Nº {ordem_nota}: {nota}")

    def exibir_menu():
        print("==========")
        print("1- Cadastrar Aluno: ")
        print("2- Lanças notas ")
        print("3- Ver Situação: ")
        print("4- Listar Alunos: ")
        print("0 - Sair!")
        print("==========")
    
    def situacao(self):
        media = sum(self.notas) / len(self.notas)
        if media <=6:
            print("Reprovado!")
        elif media >= 7 and media <=10:
            print("Aprovado!")
        else:
            print("Número inválido...")

def cadastrar_aluno():
    nome = input("Digite o seu nome: ")
    aluno = Alunos(nome)
    aluno.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso. ")
def lancar_nota():
    indice = int(input("Digite o código do aluno: "))
    aluno = aluno[indice]
    nota = float(input("Digite a nota para ser lançada: "))
    aluno.notas.append(nota)
    
aluno = []
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("encerando...")
    elif opcao == 1:
        
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def exibir(self):
        print(f"Aluno: {self.nome}")

        if self.notas:
            for ordem_nota, nota in enumerate(self.notas, 1):
                print(f"Nota Nº {ordem_nota}: {nota}")
        else:
            print("Sem notas cadastradas.")

    def situacao(self):
        if not self.notas:
            print("Aluno sem notas.")
            return

        media = sum(self.notas) / len(self.notas)

        print(f"Média: {media:.2f}")

        if media < 7:
            print("Reprovado!")
        else:
            print("Aprovado!")

    @staticmethod
    def exibir_menu():
        print("\n==========")
        print("1 - Cadastrar Aluno")
        print("2 - Lançar Nota")
        print("3 - Ver Situação")
        print("4 - Listar Alunos")
        print("0 - Sair")
        print("==========")

alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

def lancar_nota():
    indice = int(input("Digite o código do aluno: "))

    if 0 <= indice < len(alunos):
        nota = float(input("Digite a nota: "))
        alunos[indice].notas.append(nota)
        print("Nota cadastrada!")
    else:
        print("Aluno não encontrado.")

def ver_situacao():
    indice = int(input("Digite o código do aluno: "))

    if 0 <= indice < len(alunos):
        alunos[indice].situacao()
    else:
        print("Aluno não encontrado.")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos):
        print(f"\nCódigo: {i}")
        aluno.exibir()

while True:
    Aluno.exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        lancar_nota()

    elif opcao == "3":
        ver_situacao()

    elif opcao == "4":
        listar_alunos()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
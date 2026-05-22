usuario_correto = "admin"
senha_correta = "1234"

usuario = ""
senha = ""

while usuario != usuario_correto or senha != senha_correta:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario != usuario_correto or senha != senha_correta:
        print("Usuário ou senha inválidos. Tente novamente")
        
    else:
        print("Acesso liberado")
        



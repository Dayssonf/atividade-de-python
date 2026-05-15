# -------------------------
# Atividade 1 - Validação de idade
# -------------------------

while True:
    idade = int(input("Digite uma idade válida (0 a 120): "))

    if 0 <= idade <= 120:
        break
    else:
        print("Idade inválida! Tente novamente.")

print(f"Obrigado! A idade digitada foi {idade}.")


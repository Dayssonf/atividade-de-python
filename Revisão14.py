tanque = int(input("Digite a quantidade de água atual no tanque: "))
import time

while tanque > 0:
    print("Escoando 25 litro...")
    time.sleep(5)
    tanque = tanque -25
    print(f"tanque atual: {tanque}")
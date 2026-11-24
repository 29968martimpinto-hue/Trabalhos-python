import os
os.system("cls") #limpar o ecrã do terminal (

import random 
numero = random.randint(1, 100)

tentativas = 0

palpite = int(input("introduza o valor "))

while palpite != numero:
        tentativas += 1

        if palpite < numero: 
            print("Número é maior")
        elif palpite > numero:
            print("Número é menor")

        palpite = int(input("Introduzir palpite "))
       


print(f"Número Sorteado: {numero}")

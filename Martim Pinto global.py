import random
import math
import os

def CalcularRetangulo(comprimento, largura):
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)
    return area, perimetro


def CalcularResultados(a, b):
    soma = a + b
    produto = a * b
    return soma, produto



def calcular_media(notas):
    return sum(notas) / len(notas)


def contar_positivas(notas):
    return sum(1 for nota in notas if nota >= 10)

def contar_bons(notas):
    return sum(1 for nota in notas if 14 <= nota < 18)



def contar_excelentes(notas):
    return sum(1 for nota in notas if 18 <= nota <= 20)



def contar_acima_media(notas, media):
  return sum(notas) / len(notas)




def apresentar_classificacoes(notas):
    media = calcular_media(notas)
    positivas = contar_positivas(notas)
    negativas = len(notas) - positivas
    bons = contar_bons(notas)
    excelentes = contar_excelentes(notas)
    acima_media = contar_acima_media(notas, media)
    
    print("\n========== RELATÓRIO DA TURMA ==========")
    print("Lista das classificações:", notas)
    print(f"A média da turma é: {media:.2f}")
    print(f"A maior classificação: {max(notas)}")
    print(f"A menor classificação: {min(notas)}") 
    print(f"Número de classificações positivas: {positivas}")
    print(f"Número de classificações negativas: {negativas}")
    print(f"Número de alunos com classificação Bom: {bons}")
    print(f"Número de alunos com classificação Excelente: {excelentes}")
    print(f"Número de alunos acima da média: {acima_media}")
    

def executar_matematica():
    print("\n-----MATEMÁTICA-----")
    print("1 - Área de um circulo")
    print("2 - Perímetro de um circulo")
    print("3 - Raiz quadrada")
    print("4 - Potência")
    opcao = input("Escolha uma opção")




num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))

soma, produto = CalcularResultados(num1, num2)

print("A soma é:", soma)
print("O produto é:", produto)




numero = float(input("introduza um número"))

print(f"Raiz quadrada:  {math.sqrt(numero):.2f}")
print(f"Potência:  {math.pow(numero, 2):.2f}")
print(f"Valor de pi:  {math.pi:.2f}")


import statistics

notas = [12, 15, 8, 17, 14]

media = statistics.mean(notas)

print(f"Média:  {media:.2f}")



# Programa principal
comprimento = float(input("Introduza o comprimento do retângulo: "))
largura = float(input("Introduza o largura do retângulo: "))

area, perimetro = CalcularRetangulo(comprimento, largura)

print("Área do retângulo:", area)
print("Perimetro do retângulo:", perimetro)


for i in range(1, 10):
    nota = random.randint(0, 20)
    notas.append(nota)



notas=[]
opcao =""

while opcao != "0":
    os.system("cls")
    print("\n======== MENU PRINCIPAL =========")
    print("1 - Classificações")
    print("2 - Matemática")
    print("0 - Sair") 
    opçao = input("Escolha uma opção: ")

    if opcao == "1":
        apresentar_classificacoes(notas)
    elif opçao == "2":
        executar_matematica()
    elif opçao =="0":
        print("Até à próxima")
    else:
        print("Opçao inválida.")

       

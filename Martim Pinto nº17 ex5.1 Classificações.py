import random
import os
os.system("cls") # limpar ecrã do terminal


for i in range(1, 10):
    notas = random.radint(0, 20)
    notas.append(notas)

# Função para calcular a média da turma
def calcular_media(notas):
    return sum(notas) / len(notas)


# Contar classificações positivas
def contar_positivas(notas):
    return sum(1 for nota in notas if nota >= 10)


# Contar classificações Bom
def contar_bons(notas):
    return sum(1 for nota in notas if 14 <= nota < 18)


# Contar classificações Excelente
def contar_excelentes(notas):
    return sum(1 for nota in notas if 18 <= nota <= 20)


# Contar alunos acima da média
def contar_acima_media(notas, media):
  return sum(notas) / len(notas)



# Função para mostrar o relatório
def mostrar_relatorio(notas):
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


# Chamar a função para mostrar o relatório
mostrar_relatorio(notas)

print("\nTrabalho realizado por: [Martim Pinto] - [Nº17]")
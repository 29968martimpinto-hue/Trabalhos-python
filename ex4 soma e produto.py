def CalcularResultados(a, b):
    soma = a + b
    produto = a * b
    return soma, produto


# Programa principal
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))

soma, produto = CalcularResultados(num1, num2)

print("A soma é:", soma)
print("O produto é:", produto)


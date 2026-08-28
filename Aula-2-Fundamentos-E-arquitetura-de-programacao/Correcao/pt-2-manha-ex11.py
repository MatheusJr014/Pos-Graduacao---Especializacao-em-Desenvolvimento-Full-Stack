# 2. ELABORE UM ALGORITMO QUE OBTENHA O MÁXIMO DIVISOR COMUM (MDC) ENTRE DOIS NÚMEROS FORNECIDOS.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

while b != 0:
    resto = a % b
    a = b
    b = resto

print("O MDC é:", a)

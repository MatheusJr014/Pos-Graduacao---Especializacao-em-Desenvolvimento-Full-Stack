# 1. ELABORE UM ALGORITMO QUE OBTENHA O MÍNIMO MÚLTIPLO COMUM (MMC) ENTRE DOIS NÚMEROS FORNECIDOS.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

mmc = max(a, b)

while mmc % a != 0 or mmc % b != 0:
    mmc += 1

print("O MMC é:", mmc)

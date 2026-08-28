# 4. FAÇA UM ALGORITMO QUE OBTENHA O RESULTADO DE UMA EXPONENCIAÇÃO PARA QUALQUER BASE E EXPOENTE INTEIRO
# FORNECIDOS, SEM UTILIZAR A OPERAÇÃO DE EXPONENCIAÇÃO (POT).

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente inteiro: "))

resultado = 1

while expoente > 0:
    resultado *= base
    expoente -= 1

print("Resultado:", resultado)

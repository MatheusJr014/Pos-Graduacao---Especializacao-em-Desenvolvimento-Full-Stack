# 1. ELABORE UM ALGORITMO QUE OBTENHA O MÍNIMO MÚLTIPLO COMUM ((MMC)) ENTRE DOIS NÚMEROS FORNECIDOS

# o que eu quero fazer é o seguinte, tem a entrada dos 2 numeros que vai ser o calculo, e o divisor primo, e ai vai entrar dentro do while de divisão,
# onde o divisor vai ser o numero primo, e o numero1 e numero2 vão ser divididos por esse divisor, 
# e ai vai verificar se o resultado da divisão é um numero inteiro, ou seja, se o resto da divisão for 0, e ai vai continuar dividindo até que o resultado da divisão seja um numero decimal, ou seja, quando o resto da divisão for diferente de 0, ai ele vai passar para o próximo divisor primo, e ai vai continuar fazendo isso até que os dois numeros sejam iguais a 1, e ai ele vai multiplicar todos os divisores primos que foram usados para dividir os numeros, e esse resultado vai ser o MMC entre os dois numeros.

numero1 = int(input("Digite o primeiro numero para descobrir o MMC: "))
numero2 = int(input("Digite o segundo numero para descobrir o MMC: "))

# Para saber se uma divisão é exata usamos o operador módulo (%).
# Se o resto for 0, a divisão não vem "quebrada".
divisores = []

divisor = 1
while divisor <= min(numero1, numero2):
    if numero1 % divisor == 0 and numero2 % divisor == 0:
        divisores.append(divisor)
    divisor += 1

if divisores:
    maior_divisor_comum = max(divisores)
    mmc = (numero1 * numero2) // maior_divisor_comum
    print(f"O MMC entre {numero1} e {numero2} é {mmc}.")
else:
    print("Não foi possível encontrar um divisor comum.")

    


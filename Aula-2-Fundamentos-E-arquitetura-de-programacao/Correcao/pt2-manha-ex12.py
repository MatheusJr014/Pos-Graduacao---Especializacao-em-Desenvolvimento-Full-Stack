# 3. FAÇA UM ALGORITMO CAPAZ DE OBTER O QUOCIENTE INTEIRO DA DIVISÃO DE DOIS NÚMEROS FORNECIDOS,
# SEM UTILIZAR A OPERAÇÃO DE DIVISÃO (/) NEM DIVISÃO INTEIRA (DIV).

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Erro: divisão por zero.")
else:
    quociente = 0
    soma = 0

    while soma + divisor <= dividendo:
        soma += divisor
        quociente += 1

    print("O quociente é:", quociente)

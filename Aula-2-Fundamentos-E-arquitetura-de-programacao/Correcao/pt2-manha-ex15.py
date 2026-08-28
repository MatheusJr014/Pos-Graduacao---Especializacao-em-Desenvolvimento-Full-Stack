# 6. CONSTRUA UM ALGORITMO QUE, DADO UM CONJUNTO DE VALORES INTEIROS E POSITIVOS, DETERMINE O MENOR E O MAIOR
# VALOR DO CONJUNTO. O FIM DO CONJUNTO DE VALORES É CONHECIDO PELO VALOR -1, QUE NÃO DEVE SER CONSIDERADO.

valor = int(input("Digite um valor (-1 para terminar): "))

if valor == -1:
    print("Nenhum valor válido informado.")
else:
    maior = valor
    menor = valor

    while True:
        valor = int(input("Digite um valor (-1 para terminar): "))

        if valor == -1:
            break

        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

    print("Maior valor:", maior)
    print("Menor valor:", menor)

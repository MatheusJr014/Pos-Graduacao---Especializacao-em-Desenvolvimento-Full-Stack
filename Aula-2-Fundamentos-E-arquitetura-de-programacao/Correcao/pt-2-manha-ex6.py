# 2.) Elabore um algoritmo, usando a estrutura PARA, que leia um número inteiro e calcule o seu fatorial.
# Ex. o fatorial de n==5 é 120, pois: 5! = 5*4*3*2*1== 120.

n = int(input("Digite um número inteiro para calcular o fatorial: "))

if n < 0:
    print("Não existe fatorial de número negativo.")
else:
    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i

    print("O fatorial de", n, "é:", fatorial)

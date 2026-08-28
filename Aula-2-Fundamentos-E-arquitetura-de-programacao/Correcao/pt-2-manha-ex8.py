# 4.) Elabore um algoritmo, usando a estrutura PARA, que leia um número e verifique se ele é primo.
# Um número para ser primo tem no máximo dois divisores: 1 e ele próprio.

n = int(input("Digite um número inteiro: "))

if n < 2:
    print(f"O número {n} não é primo.")
else:
    contador = 0

    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1

    if contador == 2:
        print(f"O número {n} é primo.")
    else:
        print(f"O número {n} não é primo.")

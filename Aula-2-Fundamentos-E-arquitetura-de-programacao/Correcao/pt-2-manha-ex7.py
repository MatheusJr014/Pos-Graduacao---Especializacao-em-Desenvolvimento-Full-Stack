# 3.) Elabore um algoritmo, usando a estrutura PARA, que leia um número inteiro e mostre todos os seus divisores.
# Ex. se n == 20, deverá ser mostrado: 1 2 4 5 10 e 20.

n = int(input("Digite um número inteiro: "))

print("Os divisores de", n, "são:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

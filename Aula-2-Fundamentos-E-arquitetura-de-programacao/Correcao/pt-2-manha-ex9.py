# 5.) Elabore um algoritmo que leia um número inteiro e verifique se ele é ou não perfeito.
# Um número para ser perfeito deve ser igual a soma de seus divisores, exceto ele próprio.

n = int(input("Digite um número inteiro: "))

soma_divisores = 0

for i in range(1, n):
    if n % i == 0:
        soma_divisores += i

print("Soma dos divisores =", soma_divisores)

if soma_divisores == n:
    print(f"O número {n} é perfeito.")
else:
    print(f"O número {n} não é perfeito.")

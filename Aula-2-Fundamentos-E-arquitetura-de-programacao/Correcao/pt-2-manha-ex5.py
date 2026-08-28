# 1.) Elabore um algoritmo, usando a estrutura PARA, que calcule a soma de 10 números lidos pelo teclado.

soma = 0

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número: "))
    soma += num

print("A soma dos 10 números é:", soma)

# 4) Faça um algoritmo que leia dois valores inteiros e positivos e armazene nas
# variaveis A e B respectivamente. 
# Em seguida troque o conteúdo das variáveis, ou seja, 
# A deverá receber o valor de B e B o valor de A 

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

print(f"Variaveis A = {a}")
print(f"Variaveis B = {b}")
print("Realizando troca...")

temp = a
a = b
b = temp

print(f"Variaveis A = {a}")
print(f"Variaveis B = {b}")

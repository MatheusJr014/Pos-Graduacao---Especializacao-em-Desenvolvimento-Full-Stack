# 4.) Elabore um algoritmo que leia um número e calcule a soma dos número menores ou iguais a ele,
# começando pelo 1.
# Ex. para num == 10, o algoritmo devera calcular: 1+2+3+4+5+6+7+8+9+10= 55

num = int(input("Digite um número inteiro positivo: "))

soma = 0
contador = 1

while contador <= num:
    soma += contador
    contador += 1

print("A soma dos números de 1 até", num, "é:", soma)

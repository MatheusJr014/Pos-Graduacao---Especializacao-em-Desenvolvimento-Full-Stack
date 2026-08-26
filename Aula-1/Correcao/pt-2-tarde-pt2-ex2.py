# 2) Elabore um algoritmo que leia dois valores inteiros e determine qual é o maior entre eles.
 

a = float(input("informe o valor 1:"))
b = float(input("Informe o valor 2: "))



if a > b : 
    print(f"o maior valor é:", a)
elif b > a:
    print(f"o maior valor é:", b)
else:
    print("Os valores são iguais")
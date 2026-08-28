# 5) Elabore um algoritmo que leia 3 medidas (a,b,c). Verifique se elas podem ser medidas
# de um triangulo. caso sejam determine se este triangulo é equilatero, isosceles ou escaleno

a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print("As medidas formam um triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("As medidas formam um triângulo Isósceles.")
    else:
        print("As medidas formam um triângulo Escaleno.")
else:
    print("As medidas não formam um triângulo.")

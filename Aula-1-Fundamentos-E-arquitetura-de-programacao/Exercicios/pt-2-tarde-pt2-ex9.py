# 5) Elabore um algoritmo que leia 3 medidas (a,b,c). Verifique se elas podem ser medidas
# de um triangulo. caso sejam determine se este triangulo é equilatero, isosceles ou escaleno

a = float(input("Informe a medida A: "))
b = float(input("Informe a medida B: "))
c = float(input("Informe a medida C: "))

# Para formar um triângulo, cada lado deve ser menor que a soma dos outros dois
if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b and b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("As medidas não formam um triângulo")

# 2) Elabore um algoritmo que leia as medidas de um terreno retangular 
# (Comprimento e Largura) e calcule e mostre qual é o perímetro e qual é a área do terreno

comprimento = float(input(("informe o comprimento do terreno: ")))
largura = float(input(("informe a largura do terreno: ")))

area = (comprimento * largura)
perimetro = (comprimento + largura) * 2

print(f"A Aréa do Terreno é de: {area}")
print(f"O Perimetro do Terreno é de: {perimetro}")
# 1) Escreva um algoritmo que leia a altura e o sexo de uma pessoa. Calcule e imprima
# o seu peso ideal utilizando as seguintes fórmulas 

# para homens: (72.7*alt)-58;

# para mulheres: (62.1*alt)-44.7;



altura = float(input("Informe a sua altura: "))
sexo = str(input("Informe seu sexo: "))


if sexo == "masculino":
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para a sua altura é de: {peso_ideal}")
else:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para a sua altura é de: {peso_ideal}")


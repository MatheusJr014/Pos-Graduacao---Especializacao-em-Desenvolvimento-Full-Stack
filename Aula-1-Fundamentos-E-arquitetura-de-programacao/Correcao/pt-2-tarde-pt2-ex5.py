# 1) Escreva um algoritmo que leia a altura e o sexo de uma pessoa. Calcule e imprima
# o seu peso ideal utilizando as seguintes fórmulas 

# para homens: (72.7*alt)-58;

# para mulheres: (62.1*alt)-44.7;

altura = float(input("Digite a altura da pessoa (em metros): "))
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com altura {altura} m é: {peso_ideal:.2f} kg")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com altura {altura} m é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Digite M para masculino ou F para feminino.")

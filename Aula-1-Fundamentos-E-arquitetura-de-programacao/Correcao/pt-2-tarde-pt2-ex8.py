# 4) O IMC - Índice de Massa Corporal é calculado pela seguinte fórmula: 

# imc = peso / (altura * altura) 

# < 18 abaixo do peso 
# > = 18 e < 25 Peso Normal 
# > = 25 e < 30 Acima do peso 
# > = 30 Obesidade

peso = float(input("Digite o peso da pessoa (kg): "))
altura = float(input("Digite a altura da pessoa (m): "))

imc = peso / (altura * altura)

if imc < 18:
    print("IMC =", imc, "-> Abaixo do peso")
elif imc >= 18 and imc < 25:
    print("IMC =", imc, "-> Peso Normal")
elif imc >= 25 and imc < 30:
    print("IMC =", imc, "-> Acima do peso")
else:
    print("IMC =", imc, "-> Obesidade")

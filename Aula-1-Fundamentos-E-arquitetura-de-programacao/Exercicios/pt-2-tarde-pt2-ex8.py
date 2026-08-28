# 4) O IMC - Índice de Massa Corporal é calculado pela seguinte fórmula: 


# imc = peso / (altura * altura) 


# < 18 abaixo do peso 
# > = 18 e < 25 Peso Normal 
# > = 25 e < 30 Acima do peso 
# > = 30 Obesidade


peso = float(input("Informe o seu peso (kg): "))
altura = float(input("Informe a sua altura (m): "))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18:
    print("Abaixo do peso")
elif imc >= 18 and imc < 25:
    print("Peso Normal")
elif imc >= 25 and imc < 30:
    print("Acima do peso")
else:
    print("Obesidade")

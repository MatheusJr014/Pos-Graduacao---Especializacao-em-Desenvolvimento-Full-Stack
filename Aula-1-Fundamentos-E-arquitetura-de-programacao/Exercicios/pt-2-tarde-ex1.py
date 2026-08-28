# 1) Um funcionario recebe um salário fixo mais 4% de comissão sobre as vendas. 
# Faça um programa que receba o sálario fixo de um funcionário e o valor de suas vendas,
# calcule e mostre a comissão e o salário final do funcionário.



salario_fixo = float(input("Informe o sálario fixo:  "))
valor_vendas = float(input("Informe o valor de suas Vendas: "))

comissao = 0.04


salario_final = (valor_vendas * comissao) + salario_fixo

print(f"O Salario final é: {salario_final}")


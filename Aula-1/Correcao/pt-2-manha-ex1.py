#Algoritmo SalarioFuncionario


salario_fixo = float(input("Digite o salário fixo do funcionario: "))
vendas = float(input("Digite o valor total das vendas do funcionario: "))


comissao = vendas *0.04

salario_final = salario_fixo + comissao

print("Comissao sobre as Vendas: R$", comissao)
print("Salário final do funcionario: R$", salario_final)
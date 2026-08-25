# 4) Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço,
# sabendo-se que este sofreu um desconto de 10%

preco = float(input("Informe o Preço do produto: "))


desconto = 10

valor_desconto = (preco * desconto) / 100 

valor_final = preco - valor_desconto

print((f"O Valor do produto com desconto é de: {valor_final}"))
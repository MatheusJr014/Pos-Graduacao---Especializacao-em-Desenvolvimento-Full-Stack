#Fórmula do cálculo: 
#Novo Preço = preço - (preço * 10/100)

#leitura do preço do produto
print("Digite o preço do produto:")
preco = float(input())

#Cálculo do desconto de 10%
desconto = preco * 10 / 100
novo_preco = preco - desconto

#Exibição do resultado 

print("O Novo preço com 10% de desconto é:", novo_preco)

#fim
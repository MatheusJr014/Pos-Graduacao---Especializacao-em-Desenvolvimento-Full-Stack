# 3) Uma empresa de vendas oferece para seus clientes um desconto em função do valor da compra
# do cliente. Este desconto é de 25% se o valor da compra for maior ou a R$ 500,00 , 20% se for maior
# ou igual a R$ 200,00 e menor que R$ 500,00 e 15% caso seja menor que 200,00. Escreva 
# um algoritmo que imprima o valor da compra do cliente, o valor do desconto obtido e o valor a ser pago pelo cliente


valor_compra = float(input("Informe o valor da compra: "))

if valor_compra >= 500:
    desconto = valor_compra * 0.25 
    valor_final = valor_compra - desconto
    print(f"Valor com desconto: {valor_final}")
elif valor_compra >= 200 and valor_compra < 500: 
    desconto = valor_compra * 0.20 
    valor_final = valor_compra - desconto
    print(f"Valor com desconto: {valor_final}")
else: 
    desconto = valor_compra * 0.15
    valor_final = valor_compra - desconto
    print(f"Valor com desconto: {valor_final}")



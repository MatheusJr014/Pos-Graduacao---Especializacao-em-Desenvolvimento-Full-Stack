# 2) Elabore um algoritmo que leia um valor em reais (R$) e mostre sua covnersão para
# dolares ($). Para isto o algoritmo deverá solicitar ao usuário a cotação do dolar.
# Mostre o Resultado 


valor = float(input("Informe um valor a ser convertido: "))
cotacao = float(input("Cotação do Dolar: "))


valor_cotado = valor / cotacao


print(f"O valor em dolar é de: {valor_cotado}")




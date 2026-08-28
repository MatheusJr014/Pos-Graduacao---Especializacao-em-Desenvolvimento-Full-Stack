# 8. Uma rainha requisitou os serviços de um monge e disse-lhe que pagaria qualquer preço. O monge,
# necessitando de alimentos, perguntou à rainha se o pagamento poderia ser feito com grãos de trigo
# dispostos em um tabuleiro de xadrez, de tal forma que o primeiro quadro contivesse apenas um grão
# e os quadros subsequentes, o dobro do quadro anterior. A rainha concordou o pagamento baseado na
# regra estabelecida, porém percebeu, sem se dar conta, que seria impossível efetuar o pagamento.
# Faça um algoritmo para calcular o número de grãos que o monge esperava receber.

graos = 1
total_graos = 0

for casa in range(1, 65):
    print(f"Casa {casa}: {graos} grão(s)")
    total_graos += graos
    graos *= 2

print("Total de grãos:", total_graos)

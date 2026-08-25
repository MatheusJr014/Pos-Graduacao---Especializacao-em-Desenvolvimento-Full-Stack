# 3) Um motorista deseja realizar uma viagem e, com isso precisa saber quanto tempo
# levará o seu percurso. Elabore um algoritmo que leia a distancia em km e a velocidade
# média que o veiculo irá transitar e calcule e mostre o tempo da viagem 

distancia_km = float(input(("Informe a distancia em Km de Sua viagem: ")))
velocidade_media = float(input("Informe a velocidade media do seu carro: "))



tempo = distancia_km / velocidade_media

print((f"O Tempo de viagem é de: {tempo}"))


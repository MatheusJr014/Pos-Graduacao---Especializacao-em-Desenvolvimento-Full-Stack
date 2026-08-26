# 5) Escreva um algoritmo que leia um tempo em segundos e calcule o total em horas,
# minutos e segundos equivalentes a este tempo dado de entrada


segundos = float(input("Digite o Tempo em segundos: "))

horas = 3600
minutos = 60

tempo_horas = segundos / horas 

tempo_minutos = segundos / minutos

print(f"Segundos: {segundos}, Minutos: {tempo_minutos}, horas: {tempo_horas}")
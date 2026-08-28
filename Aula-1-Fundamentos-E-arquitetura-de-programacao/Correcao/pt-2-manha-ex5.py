tempo_segundos = int(input("Digite o tempo em segundos: "))

horas = tempo_segundos // 3600
resto = tempo_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print("O tempo equivalente é:", horas, "horas,", minutos, "minutos e", segundos, "segundos")

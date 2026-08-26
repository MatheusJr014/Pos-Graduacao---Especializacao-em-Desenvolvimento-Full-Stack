# 3) Elabore um algoritmo que leia um numero inteiro (max. 3 algarismos) e mostre os 
# algarismos em separado. Ex. NUM == 725 o algoritmo produzirá: Centena = 7, Dezena = 2 
# unidade = 5. 

numero = int(input("Informe um numero inteiro: "))

numero_str = str(numero)


if len(numero_str) > 3: 
    print("Máximo 3 Algarismos")
else: 
    centena = 0 
    dezena = 0 
    unidade = 0 

    if len(numero_str) == 3:
        centena = int(numero_str[0])
        dezena = int(numero_str[1])
        unidade = int(numero_str[2])
    elif len(numero_str) ==2: 
        dezena = int(numero_str[0])
        unidade = int(numero_str[1])
    else: 
        unidade = int(numero_str[0])
    print(f"Centena = {centena}, Dezena = {dezena}, Unidade = {unidade}")







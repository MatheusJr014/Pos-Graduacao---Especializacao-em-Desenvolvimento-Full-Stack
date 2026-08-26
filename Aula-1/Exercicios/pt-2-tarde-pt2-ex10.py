# 6) Elabore um algoritmo que determine se um ano é ou não bissexto. Obs. 
# Um ano é bissexto se ele for divísivel por 400 ou se ele for divisível por 4 e não por 100

ano = int(input("Informe o ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")

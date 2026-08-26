# 2) Uma competição de natação é organizada de acordo com a idade de cada nadador. 
# Elabore um algoritmo que leia a idade de um nadador e determine qual a categoria
# que ele deve competir. Considere: 




# idade < = 8 anos Categoria Infantil A
# idade < 13 anos = Categoria Infantil B
# idade < 18 anos = Categoria Juvenil A 
# idade < 21 anos = Categoria Juvenil B
# idade > = 21 Categoria Senior 


idade = int(input("Informe a sua idade: "))


if idade <= 8:
    print(f"Categoria Infantil A")
elif idade > 8 and idade < 13:
    print("Categoria Infantil B")
elif idade > 13 and idade < 18:
    print("Categorira Juvenil A")
elif idade > 18 and idade < 21:
    print("Categoria Juvenil B")
else: 
    print("Categoria Senior")


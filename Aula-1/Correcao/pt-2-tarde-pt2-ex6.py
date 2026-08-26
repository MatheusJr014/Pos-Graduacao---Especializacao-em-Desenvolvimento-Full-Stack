# 2) Uma competição de natação é organizada de acordo com a idade de cada nadador. 
# Elabore um algoritmo que leia a idade de um nadador e determine qual a categoria
# que ele deve competir. Considere: 

# idade < = 8 anos Categoria Infantil A
# idade < 13 anos = Categoria Infantil B
# idade < 18 anos = Categoria Juvenil A 
# idade < 21 anos = Categoria Juvenil B
# idade > = 21 Categoria Senior 

idade = int(input("Digite a idade do nadador: "))

if idade < 0:
    print("Idade inválida.")
elif idade <= 8:
    print("Categoria: Infantil A")
elif idade < 13:
    print("Categoria: Infantil B")
elif idade < 18:
    print("Categoria: Juvenil A")
elif idade < 21:
    print("Categoria: Juvenil B")
else:
    print("Categoria: Sênior")

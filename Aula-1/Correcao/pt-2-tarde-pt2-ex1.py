# 1) Elabore um algoritmo que leia duas notas, calcule a média e verifique se o aluno
# foi aprovado ou reprovado para estar aprovado a média deverá ser maior ou igual a 7. 

nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7: 
    print(f"Aluno Aprovado, {media}")
else:
    print(f"Aluno Reprovado, {media}")
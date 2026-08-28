# 1.) Considerando uma classe com 60 alunos, elabore um algoritmo que leia duas notas de cada aluno,
# calcule a média e verifique se aluno foi aprovado ou reprovado.
# Para estar aprovado a média deverá ser maior ou igual a 6.

contador = 1

while contador <= 60:
    print("Digite a primeira nota do aluno", contador, ":")
    nota1 = float(input())

    print("Digite a segunda nota do aluno", contador, ":")
    nota2 = float(input())

    media = (nota1 + nota2) / 2

    if media >= 6:
        print("Aluno", contador, "aprovado! Média =", media)
    else:
        print("Aluno", contador, "reprovado! Média =", media)

    contador += 1

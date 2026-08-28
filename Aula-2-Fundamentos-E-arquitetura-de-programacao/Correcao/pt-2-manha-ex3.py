# 3.) Elabore um algoritmo que melhore o algoritmo do exercício 1, calculando a média geral da classe
# (somar todas as médias e depois dividi-la pelo total de alunos da turma).

contador = 1
soma_medias = 0

while contador <= 60:
    print("Digite a primeira nota do aluno", contador, ":")
    nota1 = float(input())

    print("Digite a segunda nota do aluno", contador, ":")
    nota2 = float(input())

    media = (nota1 + nota2) / 2
    soma_medias += media

    if media >= 6:
        print("Aluno", contador, "aprovado! Média =", media)
    else:
        print("Aluno", contador, "reprovado! Média =", media)

    contador += 1

media_geral = soma_medias / 60

print("A média geral da turma é:", media_geral)

# 2.) Melhore o algoritmo do exercício 1, e determine a quantidade de alunos aprovados
# e reprovados na referida classe.

contador = 1
aprovados = 0
reprovados = 0

while contador <= 60:
    print("Digite a primeira nota do aluno", contador, ":")
    nota1 = float(input())

    print("Digite a segunda nota do aluno", contador, ":")
    nota2 = float(input())

    media = (nota1 + nota2) / 2

    if media >= 6:
        print("Aluno", contador, "aprovado! Média =", media)
        aprovados += 1
    else:
        print("Aluno", contador, "reprovado! Média =", media)
        reprovados += 1

    contador += 1

print("Total de alunos aprovados:", aprovados)
print("Total de alunos reprovados:", reprovados)

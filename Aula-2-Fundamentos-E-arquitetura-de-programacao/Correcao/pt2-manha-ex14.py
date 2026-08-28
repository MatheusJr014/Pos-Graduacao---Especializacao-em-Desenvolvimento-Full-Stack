# 5. CONSTRUA UM ALGORITMO QUE GERE OS 20 PRIMEIROS TERMOS DE UMA SÉRIE TAL QUAL A DE FIBONACCI,
# MAS CUJOS DOIS PRIMEIROS TERMOS SEJAM FORNECIDOS PELO USUÁRIO.

termo1 = int(input("Informe o primeiro termo: "))
termo2 = int(input("Informe o segundo termo: "))

print("Série gerada:", termo1, termo2, end=" ")

for cont in range(3, 21):
    proximo = termo1 + termo2
    print(proximo, end=" ")

    termo1 = termo2
    termo2 = proximo

print()

# 4) Idem ao 2) porém com três valores


v1 = int(input("informe o valor 1:"))
v2 = int(input("Informe o valor 2: "))
v3 = int(input("Informe o valor 3: "))


if v1 > v2 and v1 > v3: 
    print(f"Valor 1 é maior")
elif v2 > v1 and v2 > v3:
    print(f"Valor 2 é maior")
elif v3 > v1 and v3 > v2:
    print("Valor 3 é maior")
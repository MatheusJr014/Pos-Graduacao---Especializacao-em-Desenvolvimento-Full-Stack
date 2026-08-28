# 4) Idem ao 2) porém com três valores


a = int(input("informe o valor 1:"))
b = int(input("Informe o valor 2: "))
c = int(input("Informe o valor 3: "))


if a > b and a > c: 
    print(f"Valor a é maior")
elif b > a and b > c:
    print(f"Valor b é maior")
elif c > a and c > b:
    print("Valor c é maior")
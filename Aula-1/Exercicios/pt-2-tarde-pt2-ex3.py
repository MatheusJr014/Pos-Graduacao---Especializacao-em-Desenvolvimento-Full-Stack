# 3) Elabore um algoritmo que leia a velocidade máxima permitida em uma rodovia e 
# também a velocidade que um determinado veículo trafega. Verificar se ele sofrerá
# multa (caso em que sua velocidade seja superior a permitida) ou não.  

v1 = float(input("informe a velocidade máxima da via:"))
v2 = float(input("Velocidade que o veiculo trafega: "))





if v2 > v1 : 
    print(f"Velocidade da via ultrapassada = Multa deve ser aplicada")
else:
    print(f"Está dentro da via limite")
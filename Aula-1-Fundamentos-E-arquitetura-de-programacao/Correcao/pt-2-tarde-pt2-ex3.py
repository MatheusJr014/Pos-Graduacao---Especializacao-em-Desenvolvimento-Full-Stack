# 3) Elabore um algoritmo que leia a velocidade máxima permitida em uma rodovia e 
# também a velocidade que um determinado veículo trafega. Verificar se ele sofrerá
# multa (caso em que sua velocidade seja superior a permitida) ou não.  

velocidade_maxima = float(input("informe a velocidade máxima da via:"))
velocidade_veiculo = float(input("Velocidade que o veiculo trafega: "))





if velocidade_veiculo > velocidade_maxima : 
    print(f"Velocidade da via ultrapassada = Multa deve ser aplicada")
else:
    print(f"Está dentro da via limite")
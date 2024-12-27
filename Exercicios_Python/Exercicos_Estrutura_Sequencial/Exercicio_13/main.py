print("Programa para cálculo de aluguel de carro.\n|\nV")
nKm = float(input("Digite o número de quilômetros rodados:\n"))
nDias = float(input("Digite o número de dias com o veículo:\n"))
vFixo = float(input("Digite o valor fixo do aluguel diário:\n"))
cPKm = float(input("Digite o preço por quilômetro:\n"))
vTotal = (nKm * cPKm) + (nDias * vFixo)
print("O valor total do aluguel é " + str(vTotal) + "R$")


print("Programa de cálculo da área de um trapézio.")

bMaior = float(input("Digite o valor da base maior:\n"))
bMenor = float(input("Digite o valor da base menor:\n"))
altura = float(input("Digite a altura do trapézio:\n"))
area = (bMaior + bMenor) * altura / 2
print("O valor da área desse trapézio é de " + str(area))

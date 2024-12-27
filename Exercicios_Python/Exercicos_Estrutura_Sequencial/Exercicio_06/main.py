import math

print("Programa para cálculo da área de um hexágono regular.\n|\nV")
lado = float(input("Digite o lado do hexágono:\n"))
area = (3 * (lado ** 2) * math.sqrt(3)) / 2
print("A área desse hexágono é: " + str(area))
print("Programa para cálculo de juros simples.\n|\nV")
taxaJuros = float(input("Insira a taxa de juros em pontos percentuais:\n"))
cInicial = float(input("Insira o valor do capital inicial em reais:\n"))
tempo = int(input("Insira a qauntidade de períodos no investimento em meses:\n"))
ganho = taxaJuros * cInicial * tempo / 100
total = ganho + cInicial
print("Seu ganho foi de " + str(ganho) + "R$")
print("O montante do investimento é de " + str(total) + "R$")

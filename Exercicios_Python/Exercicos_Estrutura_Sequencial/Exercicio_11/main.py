print("Programa de cálculo de juros compostos.\n|\nV")
vInicial = float(input("Digite o valor inicial investido em reais:\n"))
taxaJuros = float(input("Digite a taxa de juros mensal em pontos percentuais:\n"))
tempoInvest = float(input("Digite o tempo de investiemto do valor em meses:\n"))
valorFinal = vInicial * ((1 + taxaJuros/100) ** tempoInvest)
vJuros = valorFinal - vInicial
print("O montante do investimento foi de " + str(valorFinal) + "R$" + " e o ganho de juros foi de " + str(vJuros) + "R$")

print("Programa para cálculo de salário líquido.\n| \nV")
sBruto = float(input("Digite o valor do salário bruto:\n"))
percDesc = float(input("Digite a soma dos percentuais dos descontos (INSS, IR, etc...):\n"))
percBen = float(input("Digite a soma dos percentuais de benefícios (vale-refeiçao, vale-transporte, etc...):\n"))
vDesc = sBruto * percDesc / 100
vBen = sBruto * percBen / 100
sLiquido = sBruto - vDesc + vBen
print("O salário líquido é: " + str(sLiquido) + ("R$\n") + "O valor dos descontos é: " + str(vDesc) + "R$\n" + "O valor dos benefícios é: " + str(vBen) + "R$" )

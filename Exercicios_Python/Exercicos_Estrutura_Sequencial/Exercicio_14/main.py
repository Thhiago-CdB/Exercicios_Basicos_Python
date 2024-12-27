print("Programa de cálculo e previsão de idade.\n|\nV")
anoNascimento = int(input("Insira seu ano de nascimento:\n"))
anoAtual = int(input("Insira o ano mais recente do seu aniverssário:\n"))
anoPrevisao = int(input("Insira o ano em qual você quer saber sua idade:\n"))
idadeAtual = anoAtual - anoNascimento
idadeFutura = anoPrevisao - anoNascimento
print("Sua idade atual é de " + str(idadeAtual) + " anos")
print("Sua idade futura é de " + str(idadeFutura) + " anos")
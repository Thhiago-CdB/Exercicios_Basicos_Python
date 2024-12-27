print("Programa de formatção de horário.\n|\nV")
qSegundos = float(input("Digite a quantidade de segundos:\n"))
horas = qSegundos // 3600
minutos = (qSegundos % 3600) // 60
segundos = qSegundos % 60
print("A quantidade de segundos informada é equivalente a: " + str(horas) + " hora(s),\n" + str(minutos) + " minuto(s) e\n" + str(segundos) + " segundo(s)")

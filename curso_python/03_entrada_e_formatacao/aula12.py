# exercicio de imc

nome = input("Digite o nome do paciente: ")
altura = str(float(input("Digite a altura do paciente: ")))
peso = str(float(input("Digite o peso do paciente: ")))

imc = float(peso) / (float(altura) ** 2)

print("O nome do paciente é " + nome + " , \nsua altura é de " + str(altura) + " metros , \nseu peso é de " + str(peso) + " kg , \ne seu imc é de " + str(imc))
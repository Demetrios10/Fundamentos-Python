# Media de Notas Com Verificação de Faltas 

nota1 = nota2 =  0.0
media = 0.0 
faltas = 0

n1 = float(input("Digite a priemira nota: "))
n2 = float(input("Digite a segunda Nota: "))
faltas = int(input("Digite Quantas faltas o Aluno Tem: "))
media = (n1 + n2)/2

if(faltas >= 10):
    print("Aluno Reprovado Por Faltas.")
elif(media >= 7):
    print("Resultado: Aprovado!")
    print("Parabens!!")
elif(media >= 5):
    print("Voce esta de Recuperação!")
else:
    print("Aluno Reprovado!")

print("A sua Média é {}".format(media))
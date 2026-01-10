# Condicionais 
# Simples , Composto , Encadeado 

nota1 = nota2 = 0.0
media = 0.0 

n1 = float(input("Digite a priemira nota: "))
n2 = float(input("Digite a segunda Nota: "))
media = (n1 + n2)/2

if(media >= 7):
    print("Resultado: Aprovado")
    print("Parabens!")
elif(media >= 5):
    print("Voce esta de Recuperação!")
else:
    print("Aluno Reprovado!")

print("A sua Média é {}".format(media))
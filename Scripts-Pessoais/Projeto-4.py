# Média Salarial

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))

if(nome == 'Demetrios' and salario <= 5.500):
    print(f'O Nome dele é {nome} e o salario dele é de um Junior {salario:.3f}')
elif(nome == 'Denis' and salario >= 8.000 or salario <= 9.000):
    print(f'O Nome dele não é {nome} e o salario dele é de um Pleno {salario:.3f}')
elif(nome == "Max" and salario >= 10.000 or salario <= 15.000):
    print(f'O nome dele é {nome} e o salario dele é de um Senior {salario:.3f}')
else:
    print('Voce digitou algum dado errado por favor redigite!!')


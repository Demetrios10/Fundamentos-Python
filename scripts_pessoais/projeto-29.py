'''
1 - Faça um programa que peça para o usuario digitar um numero inteiro e informe
se esse numero é par ou impar , caso o usuario digite um numero que não seja
inteiro informe que não é um numero inteiro.


2 - Faça um programa que pergunte a hora ao usuario e baseando-se no horario
descrito , exiba uma saudação apropriada Ex:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23

3 - Faça um programa que peça o primeiro nome de usuario .se o nome tiver
4 letras ou menos escreva "Seu nome é curto"
se tiver entre 5 e 6 letras escreva "Seu nome é normal"
maior que 6 escreva "Seu nome é muito grande".

'''

'''
numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')
'''

'''
# 2
horario = int(input('Digite um horario: '))

if horario >= 0 and horario <= 11:
    print('Bom dia')
elif horario >= 12 and horario <= 17:
    print('Boa tarde')
elif horario >= 18 and horario <= 23:
    print('Boa noite')
'''

# 3
nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')
else:
    print('Nome inválido')
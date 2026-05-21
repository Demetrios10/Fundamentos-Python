# if , else , elif
# if = se
# else = se não
# elif = se não se


entrada = input('Digite um número: ')
if entrada.isdigit():
    numero = int(entrada)
    if numero > 5:
        print('Número maior que 5')
    elif numero == 5:
        print('Número igual a 5')
    else:
        print('Número menor que 5')
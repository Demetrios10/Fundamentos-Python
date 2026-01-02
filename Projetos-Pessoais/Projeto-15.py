# Calculadora com while 

while True:
    numero1 = float(input('Digite Primeiro Numero: '))
    numero2 = float(input('Digite Segundo Numero: '))
    operador = input('Digite um Simbolo (+-/*): ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
       num1_float = float(numero1)
       num2_float = float(numero2)
       numeros_validos = True
    except:
     numeros_validos = None

    if numeros_validos is None:
       print('Um ou ambos os numeros digitados são invalidos.')
       continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador Invalido.')
        
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta ')
    if operador == '+':
       print(f'{num1_float} + {num2_float} = ', num1_float + num2_float)
    elif operador == '-':
       print(f'{num1_float} - {num2_float} = ', num1_float - num2_float)
    elif operador == '/':
       print(f'{num1_float} / {num2_float} = ', num1_float / num2_float)
    elif operador == '*':
       print(f'{num1_float} * {num2_float} = ', num1_float * num2_float)
    else:
       print('Numca Deveria Chegar aqui.')
       
    sair = input('Quer sair ? [s]im: ').lower().startswith('s')
    
    if sair is True:
     break
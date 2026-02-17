# Calculadora com while

while True:
    numero1 = int(input('Digite primeiro numero: '))
    numero2 = int(input('Digite segundo numero: '))
    simbolo = input('Digite um dos Operadores + - * /: ')
    
    if simbolo == '+':
        print(numero1 + numero2)
    elif simbolo == '-':
        print(numero1 - numero2)
    elif simbolo == '*':
        print(numero1 * numero2)
    elif simbolo == '/':
        print(numero1 / numero2)
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    
    
    
    
    
    
    
    
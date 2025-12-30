# Calculadora 

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite segundo numero: '))
sinal = input('Digite sinal: ')

if(sinal == '*'):
 print(f'\nnum1 * num2 =', (num1 * num2))
elif(sinal == '+'):
 print(f'\nnum1 + num2 =', (num1 + num2))
elif(sinal == '-'):
 print(f'\nnum1 - num2 =', (num1 - num2))
elif(sinal == '/'):
 print(f'\nnum1 / num2 =', (num1 / num2))
elif(sinal == '%'):
 print(f'\nnum1 % num2 =', (num1 % num2))
elif(sinal == '**'):
 print(f'num1 ** num2 =', (num1 ** num2))
else:
    print('Por favor digite um simbolo valido!!')
print('Obrigado!!')
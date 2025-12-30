# Calculadora 

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite segundo numero: '))
simbolo = input('Digite sinal: ')

if(simbolo == '*'):
 print(num1 * num2)
elif(simbolo == '+'):
 print(num1 + num2)
elif(simbolo == '-'):
    print(num1 - num2)
elif(simbolo == '/'):
    print(num1 / num2)
elif(simbolo == '%'):
    print(num1 % num2)
elif(simbolo == '**'):
    print(num1 ** num2)
else:
    print('Por favor digite um simbolo valido!!')
print('Obrigado!!')
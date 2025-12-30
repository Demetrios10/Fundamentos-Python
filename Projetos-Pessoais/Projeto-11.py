# Calculadora 

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite segundo numero: '))
sinal = input('Digite sinal: ')

if(sinal == '*'):
 print(num1 * num2)
elif(sinal == '+'):
 print(num1 + num2)
elif(sinal == '-'):
 print(num1 - num2)
elif(sinal == '/'):
 print(num1 / num2)
elif(sinal == '%'):
 print(num1 % num2)
elif(sinal == '**'):
 print(num1 ** num2)
else:
    print('Por favor digite um simbolo valido!!')
print('Obrigado!!')
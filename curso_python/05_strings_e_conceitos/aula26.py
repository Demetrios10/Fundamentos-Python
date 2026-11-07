# introdução ao try/except
# try tenta executa um código
# except é executado quando o try falha, ou seja, quando ocorre um erro

numero = input('Digite um número: ')
try:
    print('STR' , numero)
    numero = float(numero)
    print('FLOAT' , numero)
    print('O dobro de', numero, 'é', numero * 2)
except:
    print('isso não é um numero')



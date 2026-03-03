import sys
import os


def raizes(a,b,c):
    d = (b**2 - 4 *a*c)
    x1 = (-b + d **(1/2)) / (2 *a)
    x2 = (-b - d **(1/2)) / (2 *a)

    print(f'\nValor de x1:  {x1:.2f}')
    print(f'Valor de x2:  {x2:.2f}')

if __name__=='__main__':
    while True:
       print(f'Calcular as raizes de uma equeação de 2 grau\n')
       print(f'Equação no formato ax + bx + c = 0\n')

       try:
        a = float(input('Entre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))
       except ValueError:
        print(f'Digite somente numeros!!')
       else:
        raizes(a,b,c)
    
       while True:
         continua = input('\nDigite q para sair ou n para novo calculo: ')
         if(continua.lower()== 'q'):
           sys.exit()
         elif(continua.lower()== 'n'):
           os.system('cls')
           break
         else:
           print(f'Entrada inválida.')
   
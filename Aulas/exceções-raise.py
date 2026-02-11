from math import sqrt

class NumeroNegativoError(Exception): # personalizando uma exceção de erro 
    def __init__(self):
        pass

if __name__=='__main__':
    try:
        num = int(input('Digite um numero positivo: '))
        if num < 0:
            raise NumeroNegativoError
    
    except NumeroNegativoError:
        print(f'Foi fornecido um numnero negativo!')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print(f'Fim do cálculo.')
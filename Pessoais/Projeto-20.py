# Programa que retorna valores divididos 

def div (s,p):
    if p != 0:
        return s / p
    else:
        print('Impossivel dividir por zero!')

if __name__ == '__main__':
    a = int(input("Digite um Numero: "))
    b = int(input("Digite outro Numero: "))

    r = div(a, b)
    print(f'{a} dividido por {b} é igual a: {r}')
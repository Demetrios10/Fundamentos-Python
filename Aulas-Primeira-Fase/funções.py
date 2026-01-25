# Funções 

# Função sem argumentos 
def somando():
    print(5+10)
    print(10+100)
somando()

def chamandosobrenomes():
    print('Alves')
    print('Santos')
chamandosobrenomes()



# Função com argumentos
def soma(a,b):
    print(a+b)
soma(10,20)

def multiplica(c,d):
    print(c*d)
multiplica(25,4)

def divide(e,f):
    print(e/f)
divide(100,4)

def corcarro(monza,corsa):
    print(monza,corsa)
corcarro('Cinza','Preto')



# Função com argumentos e return
def mult(x,y):
    return x * y
x = 5
y = 8
z = mult(x,y)
print(f'O Produto de {x} e {y} é {z}')


def nomescompletos(w,s):
    return 'Deltas','Cynha'
w = 'Deltas'
s = 'Cynha'
q = w , s
print(f'Os Nomes que retornaram são {q}')


# imprimendo valores ao quadrado do que foi passado na lista 
def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados
if __name__ == '__main__':
    valores = [2,5,7,9,12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)

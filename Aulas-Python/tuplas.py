# Tuplas são imutaveis 
numeros = (2,4,6,7,9)
print(numeros)


# Operações não disponiveis na tupla , sort(),append(),reverse(),pop()

# Criando uma lista apartir de uma tupla , apos mudar a tupla para lista podemos modificar a mesma
num = list(numeros)
print(num)

# modificando
num[0] = 22
print(num)


# criando uma tupla a partir de uma lista 
lista_nomes = ['Demetrios','Bruno','Jose']
nomes = tuple(lista_nomes)
print(nomes)

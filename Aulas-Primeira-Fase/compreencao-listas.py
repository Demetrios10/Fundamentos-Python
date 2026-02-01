# exemplo 1
numeros = [1,4,7,10,12,21]
quadrados = [num**2 for num in numeros]
print(quadrados)


# Criar uma lista de numeros pares de 0 a 10 
pares = [num for num in range(11) if num % 2 == 0]
print(pares)


# exemplo com texto 
# quantas vogais existem 
frase = 'A logica é apenas o principio da sabedoria e não o seu fim.'
vogais = ['a','e','i','o','u']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possue {len (lista_vogais)} vogais')
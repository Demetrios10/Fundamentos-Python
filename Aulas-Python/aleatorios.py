import random

# print('Gerar cinco numeros aleatorios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Numero gerado: {n}')

# valor = random.random()
# print(f'Numero Gerado {round (valor * 10,3)}')

# valor = random.uniform(1,100)
# print(f'Numero: {round (valor,5)}')


# escolhe um valor dentro da lista
L = [2,4,6,9,10,13,14,15,16,19,20,21,24]
# n = random.choice(L)
# print(f'Numero escolhido: {n}')

# estrai tres valores
# n = random.sample(L,3)
# print(f'Numeros escolhidos {n}')

# Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la:')
n = random.shuffle(L)
print(L)



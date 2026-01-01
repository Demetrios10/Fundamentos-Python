# Lista de Bebidas Favoritas em ordem alfabetica 

bebidas = []

for i in range(5):
    print('Digite uma Bebida Favorita: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

print(f'Essa são as suas Bebidas favoritas em ordem alfabetica, Saude!!')
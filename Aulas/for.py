# Essa é uma lista 
lista = [2,6,9,4,0,12,3,7]
palavra = 'Boson'

for item in lista:
    print(item)

for letra in palavra:
    print(letra)

for numero in range(1,11):
    print(f'numero: {numero}')

# Gera com numeros pares
for x in range(2,20,2):
    print(x)

# tupla
pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')
for pedra in pedras:
    if(pedra == 'Quartzo'):
        continue
    print(pedra)



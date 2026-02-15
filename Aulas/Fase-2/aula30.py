# while com continue 

contador = 0

while contador < 50:
    contador += 1
    if contador == 6:
        print('não mostre o numero 6')
        continue # continue = pule o numero 6 e continue 
    if contador == 10:
        print('não mostre o numero 10')
        continue
    if contador >=  15  and contador <= 20:
        print('não mostre o numero',contador)
        continue
    print(contador)
    
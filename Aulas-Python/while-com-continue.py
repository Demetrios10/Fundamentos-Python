# usando while com continue 

contador = 0

while contador < 100:
    contador += 1

    if contador >= 10 and contador <= 27:
        print('Não vai mostrar os numeros!!')
        continue

    print(contador)

    if(contador == 40):
        break

print('Acabou')
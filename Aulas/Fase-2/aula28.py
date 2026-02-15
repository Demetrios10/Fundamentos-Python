# condicao = False # condição false não executa nada dentro do while 

contador = 0

while contador <= 10:
    contador = contador + 1
    if contador == 1:
        print('*')
    elif contador == 2:
        print('**')
    elif contador == 3:
        print('***')
    elif contador == 4:
        print('****')
    elif contador == 5:
        print('*****')
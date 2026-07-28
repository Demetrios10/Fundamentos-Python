# aula sobre while

condição = True

while condição:
    nome = input('Qual é o seu nome? ')
    print(f'Olá {nome}!')

    if nome == 'sair':
        break

print('Acabou')
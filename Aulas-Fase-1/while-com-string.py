# none é = nada 
nome = None

while True:
    nome = input('Digite seu nome , ou (x)X para parar: ')
    if(nome == 'x' or nome == 'X'):
        break
    print(f'Bem-Vindo,{nome}')
print('Até Logo!!')

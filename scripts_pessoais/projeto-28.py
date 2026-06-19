nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f' nome invertido é {nome[::-1]}')
    print(f' seu nome contem ({nome.count(" ")}) espaços?')
    print(f' seu nome contem ({len(nome)}) caracteres?')
    print(f' a primeira letra do seu nome é {nome[0]}')
    print(f' a ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')    
    
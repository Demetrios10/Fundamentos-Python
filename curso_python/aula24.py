# interpolação basica de strings

nome = input('Digite seu nome: ')
print('Olá, ' + nome + '! Seja bem-vindo(a)!')
# interpolação usando f-strings
print(f'Olá, {nome}! Seja bem-vindo(a)!')
# interpolação usando o método format()
print('Olá, {}! Seja bem-vindo(a)!'.format(nome))
# interpolação usando o operador %
print('Olá, %s! Seja bem-vindo(a)!' % nome) 

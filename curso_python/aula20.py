
# Operador Logicos = Or = Ou

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')

# tratar os dados para evitar erros
nome1 = nome1.strip().capitalize()
nome2 = nome2.strip().capitalize()

if nome1 == 'Demetrios' or nome2 == 'Deltas':
    print('Bem Vindo!')
else:
    print('Acesso Negado!')

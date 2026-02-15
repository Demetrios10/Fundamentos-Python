
nome = input('Digite seu primeiro nome: ')
quantidade_letras = int(input('Digite a quantidade de letras: '))

if quantidade_letras <= 4:
    print('Seu nome é curto')
elif quantidade_letras >= 5 and quantidade_letras <= 6:
    print('Seu nome é normal')
elif quantidade_letras > 6:
    print('Seu nome é muito grande')
  
    
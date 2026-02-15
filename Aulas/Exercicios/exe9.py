
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4 and tamanho_nome >= 1:
    print('Seu nome é curto')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
elif tamanho_nome > 6:
    print('Seu nome é muito grande')
else:
    print('Digite pelo menos uma letra!!')
  
    
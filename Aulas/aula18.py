# Operadores Lógicos 
# not - inverte expressões True vira False e False vira True

senha = input('Digite a senha: ')

if not senha:
    print('Vc não digitou nada!!')
elif senha == '12345':
    print('Vc entrou no sistema')
else:
    print('Senha errada!!')
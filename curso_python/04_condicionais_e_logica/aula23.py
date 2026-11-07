
# Operador Logico = Not in = Não em

letra = input('Digite uma letra: ')

# a letra digitada não está na lista de vogais
if letra not in ['a', 'e', 'i', 'o', 'u']:
    print('A letra digitada não é uma vogal!')
else:
    print('A letra digitada é uma vogal!')
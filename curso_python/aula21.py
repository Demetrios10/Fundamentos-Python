
# Operador Logico = Not = Não

letra = input('Digite uma letra: ')

# tratar os dados para evitar erros
letra = letra.strip().lower()

# a letra digitada não é "a"
if not letra == 'a':
    print('A letra digitada não é "a"')
else:
    print('A letra digitada é "a"')
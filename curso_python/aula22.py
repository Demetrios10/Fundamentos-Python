
# Operador Logico = in = em

cor = input('Digite uma cor: ')


# se a cor digitada estiver na lista de cores, ela é válida
if cor in ['vermelho', 'verde', 'azul']:
    print('A cor digitada é válida!')
else:
    print('A cor digitada não é válida!')
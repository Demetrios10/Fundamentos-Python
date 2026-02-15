"""
Flag (Bandeira) - Marcar um Local
None = Não valor
is e is not = é ou não é (tipo, valor,identidade)
id = Identidade
"""


# v1 = 'a'
# v2 = 'c'
# print(id(v1)) # identidade 
# print(id(v2))


condicao = True # True ou False
passou_no_if = None


if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
    
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
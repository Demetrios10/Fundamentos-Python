# Flag (Bandeira) - Marcar um local
# None = não valor
# is e is not = é ou não é (tipo , valor , identidade)
# id = identidade do objeto (local na memória)

condicao = None
passou_no_if = True

if passou_no_if:
    print('faça algo')
else:
    print('não faça algo')

if passou_no_if is None:
    print('passou no if')
else:
    print('não passou no if')